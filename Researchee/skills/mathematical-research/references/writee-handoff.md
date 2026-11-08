# Researchee → Writee research handoff

Purpose: preserve the **mathematics** and evidence so Writee can produce a manuscript independently. This is a text/document contract, **not** an actual cross-plugin API or a guarantee that either plugin has been called. Produce this when the user asks to write up completed research, to transfer findings, or to keep a reusable record for later writing.

Include only material actually established or explicitly marked unresolved:

1. **Exact original question:** objects, base field, quantifiers, assumptions, target, and requested type of result.
2. **Research outcome and scope:** Complete Solution, Partial Progress, or Unresolved Investigation; any restrictions beyond the original problem.
3. **Claims:** canonical IDs where helpful; verbatim mathematical statements, their proof status and the complete indispensable proof/construction, or a pointer to user-supplied accessible full text. Distinguish fully proved from provisional and conditional.
4. **Dependencies:** which lemmas and external results each claim uses, with noncircular proof coverage and the first open gap. If a relied-on claim is unverified, mark its dependents conditional.
5. **Reproducible evidence:** exact examples, formulas, computations, scripts/data and mathematical limits; do not infer a general theorem from limited numerical evidence.
6. **Research literature:** mathematical sources actually consulted, precise statements/theorem locations if checked, and explicit access/verification gaps. This list is **not** a complete novelty or priority search.
7. **Open questions and cautions:** critical remaining bottlenecks, counterexamples/obstructions, ambiguities, and any claims requiring independent verification.

Writee is separately responsible for selecting publication structure, checking novelty and priority, verifying complete citation and attribution, editing narrative and style, and preparing LaTeX/BibTeX manuscript files. Researchee may supply mathematics and explanations but must not pretend to have done Writee's editorial checks. Do not assert automatic transfer, plugin invocation, or shared storage unless real tools confirm it.

Suggested compact skeleton (omit empty optional fields):

```
Research Handoff
Original problem:
Outcome and exact scope:
Established claims (statements, proofs, dependencies):
Conditional or conjectural claims:
Computational / construction evidence:
Mathematical source provenance:
Unresolved gaps and caveats:
```
