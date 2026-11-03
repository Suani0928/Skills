# Explicit constructions and existence problems — on-demand guide

Use when the original problem asks whether a mathematical object exists or asks for an explicit example. Adapt to the field; the algebraic-geometric checks below apply only when relevant.

## Construction as a chain of claims

Distinguish:

1. **Candidate data:** Concrete equations, parameters, divisors, linear systems, covers, or other defining data.
2. **Realizability:** All required objects exist, with the indicated incidence and compatibility conditions.
3. **Well-defined construction:** Maps, covers, gluings, or families exist as claimed; required integrality/linear-equivalence conditions hold.
4. **Geometric validity:** Smoothness, normality, irreducibility, connectedness, projectivity, and other relevant properties are proved for the correct object.
5. **Exact target properties:** Required invariants, minimality, type, automorphisms, fixed loci, branch structure, and classifications are checked.
6. **Field fidelity:** The result is defined over the required base field, not merely over a computationally convenient substitute.

Do not claim success until every item required by the user's target is justified. A candidate may still be valuable as partial progress, but must be labeled accordingly.

## Optional checklist for algebraic surfaces and double covers

For a proposed double cover of a surface, explicitly identify the base surface, branch divisor, the line bundle/divisor class defining the cover (and the correct linear equivalence), and the resulting model. Verify singularities and their resolutions, the relevant canonical divisor formula, invariants, nefness/bigness or general type, and minimality of the **correct smooth model**. Distinguish the quotient, a resolution of the quotient, the cover, and its minimal model. Count fixed curves and isolated fixed points from the actual involution, not only from expected numerical data.

In particular, checking intersection numbers, genera, or parity does not establish that a desired branch divisor or smooth minimal cover exists. If the task is over `C`, a construction over `F_p` is a **finite-field candidate**, not the requested complex example. A characteristic-zero conclusion requires a valid lifting or alternative construction and verification that the demanded properties survive.

## Nonexistence

An exhaustive obstruction argument must cover every permitted construction, not only a favorite ansatz or a finite experimental search. State explicitly the class actually ruled out if the conclusion is narrower than the original problem.
