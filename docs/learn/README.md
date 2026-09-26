# A physicist's route to Monster correlation rigidity

**Start with correlation functions, not the Monster group.** The question is whether a small amount of interaction data can identify an exact chiral theory within a specified class. The result is conditional: the class is assumed, and suitable fields must actually be supplied. Their existence is not inferred from the spectrum alone.

This path assumes quantum-mechanical states and inner products, elementary linear algebra, differentiation, and some familiarity with complex coordinates. It does not assume prior VOA, finite-group, or moonshine expertise. Complex mode notation is introduced when needed; the quantitative geometry takes place in a real finite-dimensional inner-product space.

## The two anchors

**Primary anchor:** Matthias R. Gaberdiel, [*An Introduction to Conformal Field Theory*, arXiv:hep-th/9910156v2](https://arxiv.org/html/hep-th/9910156v2). Read it in small selections alongside the lessons below, rather than finishing the whole review first.

**Secondary anchor:** Hiroshi Yamauchi, [*3-transposition groups arising in VOA theory*, arXiv:2201.06887v1](https://arxiv.org/html/2201.06887v1), selected parts of Section 4. This is a guided supplement for the special weight-two and Ising structure, not a second prerequisite course. The local lessons explain the facts needed to follow the argument. Proof-level source checking is a separate route.

| Local lesson | Primary reading in Gaberdiel | Question to answer before moving on |
|---|---|---|
| [1. What are the data?](01_correlations.md) | Sections 2.1, 3.1, 3.4, 3.5 | What is left after the position dependence of a correlator is removed? |
| [2. Turn fields into geometry](02_weight_two.md) | Section 3.6; revisit 3.4 | Why do we subtract the stress tensor and then normalize? |
| [3. Why does Ising appear?](03_ising.md) | Sections 3.7.3 and 4.4 | How can a bound on a cubic know about an internal central charge? |
| [4. From nearly extremal to exact](04_rounding.md) | No new chapter required | How do continuous error bounds force a discrete exact structure? |
| [5. Work through the certificate](05_worked_certificate.md) | Use the earlier sections as needed | Can I propagate the three error budgets and explain a failed test? |

For Lesson 3, Yamauchi Section 4, equation (4.2), Lemma 4.3, and equations (4.8)–(4.9) provide the algebraic supplement. For Lesson 4, consult Theorem 4.6 and its overlap table. Group presentations, conjugacy-class calculations, and the later 3-transposition constructions are not prerequisites for this result.

Gaberdiel Sections 3.2–3.3 support the underlying OPE construction and can be read on a second pass. Section 3.9 supplies orbifold and moonshine context, not a necessary calculation in our quantitative argument. Appendix A discusses rationality terminology. A full course on modular forms, Zhu's algebra, or fusion categories is not required before starting these lessons.

## The result before the notation

Inside the exact class described in [Assumptions and source roles](assumptions_and_sources.md), take two real, normalized weight-two primary fields. Suppose their self-three-point coefficients are sufficiently close to the maximal allowed value, and their mutual two-point coefficient is close to a particular negative number. Then nearby exact Ising directions exist; their associated Ising stress tensors are forced to be orthogonal. A prior classification theorem then identifies the underlying VOA as moonshine.

The negative number is not an unexplained fit. [Lesson 3](03_ising.md) derives it by subtracting the common ambient stress tensor from an orthogonal Ising pair.

The new quantitative step and the old classification have different jobs. The classification starts with exact internal subalgebras. The project explains when imperfect coefficient information is sufficient to recover those exact hypotheses. The [canonical core proof](../../research/uniform_extraction_core.md) specifies all constants and dependencies.

## How to use the lessons

Each lesson has one central question, a calculation, and two self-checks with expandable answers. Read the physical explanation first. Details marked as a second pass can be postponed without losing the main argument. The exercises test understanding; they are not an assessment of mathematical background.

At the end, you should be able to explain why normalization matters, why a nearly maximal coefficient locates an exact Ising direction, why the overlap gap forces orthogonality, and why a finite list of coefficients does not certify all the ambient axioms.

Then read the [core proof](../../research/uniform_extraction_core.md), followed by [sharpness and calibration](../../research/sharpness_and_calibration.md). The [research status](../RESEARCH_STATUS.md), [contribution comparison](../../audits/quantitative_contribution_verdict.md), and [final bounded review](../../audits/final_quantitative_review.md) belong to the research-checking route, not the first lesson.

The teaching notes explain the existing theorem. They do not replace its exact hypotheses or re-prove its imported classification theorems. Manuscript writing remains on hold. Questions and corrections may be sent to Ruge Lin at gogoko699@gmail.com.
