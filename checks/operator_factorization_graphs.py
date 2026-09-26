"""Exact tensor-contraction certificate for the six-label operator identity.

A monomial is a graph of copies of one REAL symmetric cubic C and Kronecker
contractions. Its value is a finite Einstein sum. The reduction rules are the
stated trace identities; their numerical coefficients are hypotheses, not
learned from a small example. Boundary projections are explicit finite signed
averages. This is a reproducible symbolic certificate, not a proof-assistant
formalization or a construction of the 196883-dimensional multiplication.

Only Python's standard library is needed for the symbolic certificate.
The independent direct-matrix controls in the caller use NumPy object arrays.
"""
from fractions import Fraction as Q
from collections import defaultdict,Counter
from functools import lru_cache
from itertools import combinations, permutations
import itertools

# Each C is a trivalent vertex; negative integers are fixed external labels.
# An edge contracts two indices using the positive Euclidean metric.
# Graph isomorphisms rename dummy indices only.

D=196883; KAPPA=Q(13858,3); NU=Q(899); ALPHA=Q(496,3); BETA=Q(-116); U=Q(965,9); V=Q(40,3); GAMMA=Q(1,3)
# Exterior vectors a,...,f supply six distinguished one-valent boundary vertices -1..-6.
COUNTER=itertools.count(100)
def fresh():return next(COUNTER)

def addterms(*polys):return sum(polys,[])
def times(p,q):return [(a*b,cs+ds,es+fs) for a,cs,es in p for b,ds,fs in q]
def scale(p,a):return [(a*c,vs,ds) for c,vs,ds in p if a*c]
def wedge(a,b,i,j):return [(Q(1),(),((i,a),(j,b))),(Q(-1),(),((i,b),(j,a)))]
def leftL(a,x,i,j):
 k=fresh();return [(Q(1),((a,i,k),),())], x(k,j)
def Dact(a,x,i,j):
 k=fresh();l=fresh()
 return addterms(times([(Q(1),((a,i,k),),())],x(k,j)),times(x(i,l),[(Q(1),((a,l,j),),())]))
def F(x,i,j):
 k,l,t=fresh(),fresh(),fresh()
 return times([(Q(1),((t,i,k),(t,l,j)),())],x(k,l))
def G(x,i,j):return addterms(F(x,i,j),scale(x(i,j),GAMMA))
def mul(x,y,i,j):
 k=fresh();return times(x(i,k),y(k,j))
def ad(x,y,i,j):return addterms(mul(x,y,i,j),scale(mul(y,x,i,j),-1))

def canon_edges(n,edges):
 edges=tuple(sorted(tuple(sorted(e)) for e in edges));return _canon(n,edges)
@lru_cache(None)
def _canon(n,edges):
 adj={i:[] for i in range(n)}
 for a,b in edges:
  if a>=0:adj[a].append(b)
  if b>=0:adj[b].append(a)
 # canonical partition refinement; boundary vertices keep distinct names
 def refine(part):
  while True:
   colors={v:k for k,cell in enumerate(part) for v in cell}
   new=[]
   for cell in part:
    groups=defaultdict(list)
    for v in cell:
     sig=tuple(sorted(((-1,x) if x<0 else (0,colors[x])) for x in adj[v]))
     groups[sig].append(v)
    for sig in sorted(groups):new.append(tuple(groups[sig]))
   if len(new)==len(part):return tuple(new)
   part=tuple(new)
 def rec(part):
  part=refine(part)
  if len(part)==n:
   mp={v:i for i,(v,) in enumerate(part)}
   return tuple(sorted(tuple(sorted((mp.get(a,a),mp.get(b,b)))) for a,b in edges))
  idx=next(i for i,c in enumerate(part) if len(c)>1);cell=part[idx]
  vals=[]
  for v in cell:
   pp=part[:idx]+((v,),tuple(x for x in cell if x!=v))+part[idx+1:]
   vals.append(rec(pp))
  return min(vals)
 if n==0:return (0,edges)
 return (n,rec((tuple(range(n)),)))

def normalize(cs,delta,free=tuple(range(-6,0)),loop_dimension=D):
 # Union the index variables related by Kronecker deltas.
 parent={}
 def root(x):
  if x not in parent:parent[x]=x
  if parent[x]!=x:parent[x]=root(parent[x])
  return parent[x]
 def union(a,b):
  a,b=root(a),root(b)
  if a!=b:parent[b]=a
 for t in cs:
  for x in t:root(x)
 for a,b in delta:union(a,b)
 # all six boundary indices must occur once in a full monomial
 for x in free:root(x)
 ends=defaultdict(list)
 for i,t in enumerate(cs):
  for x in t:ends[root(x)].append(i)
 for x in free:ends[root(x)].append(x)
 coefficient=Q(1);edges=[]
 for r in {root(x) for x in parent}:
  vv=ends[r]
  if len(vv)==0:coefficient*=loop_dimension
  elif len(vv)==2:
   edges.append(tuple(vv))
  else:raise ValueError(('bad degree',vv,cs,delta))
 return coefficient,canon_edges(len(cs),edges)

def combine(poly,free=tuple(range(-6,0))):
 out=defaultdict(Q)
 for c,cs,de in poly:
  if c:
   f,g=normalize(cs,de,free);out[g]+=c*f
 return {g:c for g,c in out.items() if c}

def graph_tensors(g):
 n,edges=g;cs=[[] for _ in range(n)];de=[]
 for k,(a,b) in enumerate(edges):
  if a<0 and b<0:de.append((a,b));continue
  idx=a if a<0 else 1000+k
  if a>=0:cs[a].append(idx)
  if b>=0:cs[b].append(idx)
 return tuple(map(tuple,cs)),tuple(de)

def cycles(g,maxlen=4):
 n,edges=g;cnt=Counter(edges)
 loops=[(a,) for a,b in edges if a==b and a>=0]
 if loops:return sorted(set(loops))
 doubles=[(a,b) for (a,b),c in cnt.items() if a>=0 and b>=0 and c>=2]
 if doubles:return sorted(doubles)
 adj={i:set() for i in range(n)}
 for a,b in edges:
  if a>=0 and b>=0:adj[a].add(b);adj[b].add(a)
 found=set()
 def go(path,target):
  if len(path)==target:
   if path[0] in adj[path[-1]]:found.add(min(tuple(path),tuple([path[0]]+list(reversed(path[1:])))))
   return
  for nxt in sorted(adj[path[-1]]):
   if nxt>path[0] and nxt not in path:go(path+[nxt],target)
 for size in range(3,maxlen+1):
  for i in range(n):go([i],size)
  if found:return sorted(found)
 return []

def replace_cycle(g,cyc):
 if len(cyc)==1:return {}
 cs,de=graph_tensors(g);free=tuple(sorted({v for e in g[1] for v in e if v<0}));cycle_indices=[]
 k=len(cyc)
 if k==2:
  shared=list((Counter(cs[cyc[0]]) & Counter(cs[cyc[1]])).elements())
  cycle_indices=shared[:2]
 else:
  for i in range(k):
   shared=set(cs[cyc[i]]) & set(cs[cyc[(i+1)%k]])
   if len(shared)!=1:raise ValueError('cycle shared')
   cycle_indices.append(next(iter(shared)))
 slots=[]
 for i,v in enumerate(cyc):
  rem=list(cs[v])
  if k==2:
   for t in cycle_indices:rem.remove(t)
  else:
   rem.remove(cycle_indices[i]);rem.remove(cycle_indices[(i-1)%k])
  if len(rem)!=1:raise ValueError('remaining')
  slots.append(rem[0])
 base=tuple(c for i,c in enumerate(cs) if i not in cyc)
 if k==2:
  return combine([(KAPPA,base,de+((slots[0],slots[1]),))],free)
 if k==3:
  return combine([(NU,base+(tuple(slots),),de)],free)
 a,b,c,d=slots;t=99999
 terms=[(ALPHA,base+((a,b,t),(c,d,t)),de),(ALPHA,base+((a,d,t),(b,c,t)),de),
        (BETA,base+((a,c,t),(b,d,t)),de),
        (U,base,de+((a,b),(c,d))),(U,base,de+((a,d),(b,c))),(V,base,de+((a,c),(b,d)))]
 return combine(terms,free)

REDUCTION_COUNTS=Counter()
REDUCTION_DAG={}
@lru_cache(None)
def reduce(g):
 cy=cycles(g)
 if not cy:return {g:Q(1)}
 cc=cy[0];REDUCTION_COUNTS[len(cc)]+=1
 step=replace_cycle(g,cc)
 REDUCTION_DAG[g]=(cc,step)
 result=defaultdict(Q)
 for gg,ccoeff in step.items():
  for hh,dd in reduce(gg).items():result[hh]+=ccoeff*dd
 return {g:c for g,c in result.items() if c}

def reduce_poly(poly):
 """Use only the degree-one through degree-four local trace identities."""
 out=defaultdict(Q)
 for g,c in poly.items():
  for h,a in reduce(g).items():out[h]+=c*a
 return {g:c for g,c in out.items() if c}

def residual():
 x=lambda i,j:wedge(-1,-2,i,j)
 y=lambda i,j:wedge(-3,-4,i,j)
 z=lambda i,j:wedge(-5,-6,i,j)
 gy=lambda i,j:G(y,i,j)
 gz=lambda i,j:G(z,i,j)
 gx=lambda i,j:G(x,i,j)
 first=lambda i,j:Dact(-1,lambda k,l:G(lambda p,q:Dact(-2,gy,p,q),k,l),i,j)
 second=lambda i,j:Dact(-2,lambda k,l:G(lambda p,q:Dact(-1,gy,p,q),k,l),i,j)
 q=lambda i,j:addterms(first(i,j),scale(second(i,j),-1))
 op=lambda i,j:addterms(scale(q(i,j),9),scale(ad(x,gy,i,j),24336),scale(ad(gx,gy,i,j),-2704))
 i,j=fresh(),fresh()
 return combine(scale(times(gz(i,j),op(j,i)),Q(-1,2)))



# Boundary character: alternate within each pair, and between last two pairs.
def permmap(bits,exchange):
 labels=list(range(-1,-7,-1));sign=1
 for j,b in enumerate(bits):
  if b:labels[2*j],labels[2*j+1]=labels[2*j+1],labels[2*j];sign*=-1
 if exchange:labels[2:4],labels[4:6]=labels[4:6],labels[2:4];sign*=-1
 return {-(i+1):v for i,v in enumerate(labels)},sign
GROUP=[permmap(bits,e) for bits in itertools.product((0,1),repeat=3) for e in (0,1)]
@lru_cache(None)
def bcanon(g):
 n,ed=g;best=None;sgn=None
 for p,s in GROUP:
  new=canon_edges(n,[(p.get(a,a),p.get(b,b)) for a,b in ed])
  if best is None or new<best:best=new;sgn=s
  elif new==best and s!=sgn:return None,0
 return best,sgn

def project(poly):
 out=defaultdict(Q)
 for g,c in poly.items():
  h,s=bcanon(g)
  if s:out[h]+=c*s
 return {g:c for g,c in out.items() if c}


# Fifth identity used only AFTER removing its fully alternating part.
def remove_cycle(g,cyc):
 cs,de=graph_tensors(g);k=len(cyc);between=[]
 for i in range(k):
  shared=set(cs[cyc[i]])&set(cs[cyc[(i+1)%k]])
  between.append(next(iter(shared)))
 slots=[]
 for i,v in enumerate(cyc):
  rem=list(cs[v]);rem.remove(between[i]);rem.remove(between[(i-1)%k]);slots.append(rem[0])
 return tuple(c for i,c in enumerate(cs) if i not in cyc),de,slots

def trace_cycle(slots):
 n=len(slots);ind=list(range(100000,100000+n))
 return tuple((slots[i],ind[i],ind[(i+1)%n]) for i in range(n))
def lower_terms(base,de,slots):
 poly=[]
 for s in range(5):
  a,b,c,d,e=slots[s:]+slots[:s]
  # H(a,b;c;d,e) = C(a,b,r) C(r,c,t) C(t,d,e)
  for coeff,pair1,center,pair2 in [(Q(89,3),(a,b),c,(d,e)),(Q(4),(a,d),c,(b,e)),(Q(-22),(a,e),c,(b,d))]:
   r,t=200000,200001
   poly.append((coeff,base+((pair1[0],pair1[1],r),(r,center,t),(t,pair2[0],pair2[1])),de))
  poly.append((Q(185,9),base+((c,d,e),),de+((a,b),)))
  poly.append((Q(10,3),base+((b,d,e),),de+((a,c),)))
 return poly

def sgn(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
PERMS=[]
for p in permutations(range(1,5)):
 seq=(0,)+p
 if seq[1]<seq[-1]:PERMS.append((seq,sgn(seq)))
if len(PERMS)!=12: raise RuntimeError('Wrong pentagon dihedral representatives')


def fifth_relation(g,cyc):
 """Return the expanded nonalternating fifth trace in a closed context.

 The 12 representatives enumerate S5/D5; the coefficient 1/12 is the
 normalized signed alternating trace. The five-form coefficient (26 versus
 52 in competing conventions) never appears in this relation.
 """
 base,de,slots=remove_cycle(g,cyc)
 poly=[(Q(1),base+trace_cycle(slots),de)]
 for perm,sign in PERMS:
  poly.append((-Q(sign,12),base+trace_cycle([slots[i] for i in perm]),de))
 poly+=scale(lower_terms(base,de,slots),-1)
 return reduce_poly(combine(poly,free=()))

def glue(g,h,permutation,loop_dimension=D):
 """Contract all six boundaries of two tensors, with a chosen permutation."""
 gc,gd=graph_tensors(g);hc,hd=graph_tensors(h)
 def mp(v): return permutation[v] if v<0 else v+10000
 hc=tuple(tuple(mp(v) for v in t) for t in hc)
 hd=tuple(tuple(mp(v) for v in t) for t in hd)
 return normalize(gc+hc,gd+hd,free=(),loop_dimension=loop_dimension)

def component(kind):
 """Six-label tensor <G(e wedge f), O_(a wedge b) G(c wedge d)>.

 O is Q_x, ad_x, or ad_(Gx), in that order. The exterior inner product
 is half Frobenius, equivalently -tr(XY)/2 on skew matrices.
 """
 x=lambda i,j:wedge(-1,-2,i,j)
 y=lambda i,j:wedge(-3,-4,i,j)
 z=lambda i,j:wedge(-5,-6,i,j)
 gy=lambda i,j:G(y,i,j)
 gz=lambda i,j:G(z,i,j)
 gx=lambda i,j:G(x,i,j)
 if kind=='Q':
  first=lambda i,j:Dact(-1,lambda k,l:G(lambda p,q:Dact(-2,gy,p,q),k,l),i,j)
  second=lambda i,j:Dact(-2,lambda k,l:G(lambda p,q:Dact(-1,gy,p,q),k,l),i,j)
  op=lambda i,j:addterms(first(i,j),scale(second(i,j),-1))
 elif kind=='x':op=lambda i,j:ad(x,gy,i,j)
 elif kind=='Gx':op=lambda i,j:ad(gx,gy,i,j)
 else:raise ValueError('Unknown operator component')
 i,j=fresh(),fresh()
 return combine(scale(times(gz(i,j),op(j,i)),Q(-1,2)))

def norm_polynomial(first,second,loop_dimension=D):
 """Exact inner product of boundary-projected six-index tensors."""
 poly=defaultdict(Q)
 for g,c in first.items():
  for h,a in second.items():
   for perm,sign in GROUP:
    fac,gg=glue(g,h,perm,loop_dimension=loop_dimension)
    poly[gg]+=c*a*Q(sign,16)*fac
 return {g:c for g,c in poly.items() if c}

# The three irreducible closed graphs that survive the short-cycle reduction.
# Labels are vertex indices, not group elements. Each has degree three.
EMPTY=(0,())
P10=(10,((0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9),
          (4,6),(4,8),(5,7),(5,9),(6,9),(7,8)))
A12=(12,((0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9),
          (4,6),(4,8),(5,7),(5,9),(6,10),(7,11),(8,11),(9,10),(10,11)))
B12=(12,((0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,8),(3,7),(3,9),
          (4,6),(4,11),(5,7),(5,10),(6,10),(7,11),(8,9),(8,11),(9,10)))
PENTAGON=(0,1,4,6,2)
SCALAR_GRAPHS=(EMPTY,P10,A12,B12)

def solve_system(matrix,rhs):
 """Small exact Gaussian elimination, with singularity detection."""
 n=len(rhs);rows=[list(map(Q,row))+[Q(b)] for row,b in zip(matrix,rhs)]
 determinant=Q(1)
 for k in range(n):
  pivot=next((j for j in range(k,n) if rows[j][k]),None)
  if pivot is None:raise ArithmeticError('Singular certificate system')
  if pivot!=k:rows[k],rows[pivot]=rows[pivot],rows[k];determinant=-determinant
  p=rows[k][k];determinant*=p;rows[k]=[x/p for x in rows[k]]
  for j in range(n):
   if j!=k:
    p=rows[j][k]
    rows[j]=[a-p*b for a,b in zip(rows[j],rows[k])]
 return [row[-1] for row in rows],determinant

def encode_graph(g): return {'vertices':g[0],'edges':[list(e) for e in g[1]]}
def encode_poly(poly):
 return [{'coefficient':str(c),'graph':encode_graph(g)} for g,c in sorted(poly.items()) if c]

def build_certificate():
 """Recompute all diagrams, short-cycle reductions, and the three trace-five rows."""
 components=[project(component(kind)) for kind in ('Q','x','Gx')]
 relations=[fifth_relation(g,PENTAGON) for g in SCALAR_GRAPHS[1:]]
 for row in relations:
  if set(row)-set(SCALAR_GRAPHS):raise ArithmeticError('Unresolved scalar contraction')
 mat=[[row.get(g,Q(0)) for g in SCALAR_GRAPHS[1:]] for row in relations]
 rhs=[-row.get(EMPTY,Q(0)) for row in relations]
 sol,determinant=solve_system(mat,rhs)
 values={EMPTY:Q(1),**dict(zip(SCALAR_GRAPHS[1:],sol))}
 inner=[];reduced=[];raw=[]
 for i in range(3):
  rr=[];pp=[];rawrow=[]
  for j in range(3):
   polynomial=norm_polynomial(components[i],components[j])
   red=reduce_poly(polynomial)
   if set(red)-set(values):raise ArithmeticError('Unresolved Gram contraction')
   rr.append(sum((c*values[g] for g,c in red.items()),Q(0)))
   pp.append(red);rawrow.append(polynomial)
  inner.append(rr);reduced.append(pp);raw.append(rawrow)
 factors=(Q(9,2704),Q(9),Q(1))
 common=Q(107700439863024387072)
 gram=[[inner[i][j]*factors[i]*factors[j]/common for j in range(3)] for i in range(3)]
 return {'components':components,'relations':relations,'relation_matrix':mat,'relation_rhs':rhs,
         'relation_determinant':determinant,'values':values,'raw_gram':raw,'reduced_gram':reduced,
         'unscaled_gram':inner,'rescaling':factors,'common_factor':common,'small_gram':gram}
