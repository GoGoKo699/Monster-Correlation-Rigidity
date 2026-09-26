"""Exact Virasoro certificate for a triple of weight-three primaries.

The PBW/vacuum-mode implementation follows the algorithm in pending PR14,
checks/mixed_trace_virasoro.py (e608dec), generalized here to arbitrary primary
weights. All coefficients are formal multiples of <a,b_(hb+hc-ha-1)c>.
No division by a physical correlation coefficient and no floating point.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb

def bc(n,k):
 if k<0:return 0
 if n>=0:return comb(n,k) if k<=n else 0
 return (-1)**k*comb(k-n-1,k)
def add(*terms):
 out={}
 for c,s in terms:
  for w,v in s.items():out[w]=out.get(w,F(0))+c*v
 return {w:v for w,v in out.items() if v}
class Vir:
 def __init__(self,c=24,h=0):self.c,self.h=F(c),F(h)
 @lru_cache(None)
 def ins(self,k,word):
  if not word:return {} if k==1 and self.h==0 else {(k,):F(1)}
  b,tail=word[0],word[1:]
  if k>=b:return {(k,)+word:F(1)}
  return add((1,self.apply(-b,self.ins(k,tail))),(b-k,self.ins(k+b,tail)))
 @lru_cache(None)
 def act(self,m,word):
  if m<0:return self.ins(-m,word)
  if m==0:return {word:self.h+sum(word)} if self.h+sum(word) else {}
  if not word:return {}
  k,rest=word[0],word[1:]
  out=add((1,self.apply(-k,self.act(m,rest))),(m+k,self.act(m-k,rest)))
  if m==k:out=add((1,out),(self.c*F(m**3-m,12),{rest:F(1)}))
  return out
 def apply(self,m,state):return add(*[(v,self.act(m,w)) for w,v in state.items()])
 def gram(self,left,right):
  s={right:F(1)}
  for m in left:s=self.apply(m,s)
  return s.get((),F(0))
 @lru_cache(None)
 def mode(self,lam,index,word):
  if not lam:return {word:F(1)} if index==-1 else {}
  m,rest=lam[0],lam[1:];k,weight,level=m-2,sum(rest),sum(word);out={}
  for j in range(max(-1,level+weight-index-1)+1):
   out=add((1,out),(bc(j+k,k),self.apply(-j-m,self.mode(rest,index+j,word))))
  for j in range(k,level+m):
   inner=self.act(j-m+1,word)
   term=add(*[(v,self.mode(rest,index-1-j,w)) for w,v in inner.items()])
   out=add((1,out),((-1)**k*bc(j,k),term))
  return out
@lru_cache(None)
def parts(n,top=None):
 if n==0:return ((),)
 if n<2:return ()
 top=n if top is None else top
 return tuple((k,)+tail for k in range(min(top,n),1,-1) for tail in parts(n-k,k))
def solve(M,rhs):
 rows=[list(map(F,r))+[F(b)] for r,b in zip(M,rhs)];n=len(rhs)
 for i in range(n):
  pivot=next(j for j in range(i,n) if rows[j][i]);rows[i],rows[pivot]=rows[pivot],rows[i];v=rows[i][i];rows[i]=[x/v for x in rows[i]]
  for j in range(n):
   if j!=i:
    v=rows[j][i];rows[j]=[a-v*b for a,b in zip(rows[j],rows[i])]
 return [r[-1] for r in rows]
# t=<a,b_(h_b+h_c-h_a-1)c> for primary a,b,c, real PCT-fixed.
# <0,a_p b_q c> =(-1)^ha binom(h_a+h_b-h_c + l-1,l)*t ; p=2ha-1+l.
# Interchanging the first two labels changes this Hermitian-state convention
# by (-1)^hc; it is not the unadjusted sphere-correlator permutation rule.
@lru_cache(None)
def ward(left,p,q,ha,hb,hc,swap=False):
 if not left:
  if p+q!=ha+hb+hc-2:return F(0)
  lev=p-(2*ha-1)
  if lev<0:return F(0)
  return F((-1)**ha*bc(ha+hb-hc+lev-1,lev))*((-1)**hc if swap else 1)
 m,rest=left[-1],left[:-1]
 return ((ha-1)*(m+1)-p)*ward(rest,p+m,q,ha,hb,hc,swap)+((hb-1)*(m+1)-q)*ward(rest,p,q+m,ha,hb,hc,swap)
def composite(lam,r,s,ha,hb,hc):
 left=tuple(reversed(lam));out=F(0)
 for k in range(max(hb+hc-1-s,ha+hc-1)+1):
  c=(-1)**k*bc(r,k)
  if k<=hb+hc-1-s:out+=c*ward(left,r-k,s+k,ha,hb,hc)
  if k<=ha+hc-1:out-=c*(-1 if r % 2 else 1)*ward(left,r+s-k,k,hb,ha,hc,True)
 return out

def reconstruct(ha=3, hb=3, hc=3):
    vac, primary = Vir(24, 0), Vir(24, 2)
    rows, total = [], F(0)
    for n in range(hc, ha+hb+hc+1):
        basis = parts(n)
        gram = [[vac.gram(a, b) for b in basis] for a in basis]
        rhs = [sum((F(bc(ha,i)*bc(ha+hb-i,j))*composite(lam,i-1,j-1,ha,hb,hc)
                    for i in range(ha+1) for j in range(ha+hb-i+1)
                    if ha+hb+hc-i-j == n), F(0)) for lam in basis]
        projection = solve(gram, rhs)
        vacuum_trace = [vac.mode(lam,n-1,(2,)).get((2,),F(0)) for lam in basis]
        primary_trace = [primary.mode(lam,n-1,()).get((),F(0)) for lam in basis]
        trace = [v+196883*p for v,p in zip(vacuum_trace,primary_trace)]
        contribution = sum((a*b for a,b in zip(projection,trace)), F(0))
        total += contribution
        rows.append({'weight':n,'partitions':basis,'gram':gram,'pairing':rhs,
                     'projection':projection,'zero_mode_trace':trace,
                     'vacuum_contribution':sum((a*b for a,b in zip(projection,vacuum_trace)),F(0)),
                     'per_primary_contribution':sum((a*b for a,b in zip(projection,primary_trace)),F(0)),
                     'contribution':contribution})
    return total, rows
