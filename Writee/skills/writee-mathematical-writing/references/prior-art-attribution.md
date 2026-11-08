# Prior-art detection and mandatory attribution

## Foundational rule

**A valid proof is not a novelty certificate.** Research may independently rediscover an existing theorem. The literature's prior work deserves attribution even when the manuscript contains a rewritten, reconstructed, shorter, independent, or otherwise alternative proof. It must appear in both the relevant **body text** and the **references** when the source can be verified. Never erase citation obligations in the name of stylistic concision.

## Claims subject to screening

Screen each *substantial* main theorem, independently interesting proposition, nontrivial imported lemma, important method or construction, and specific historical/priority claim. For standard facts, judge whether a citation is helpful for target readership; no requirement to cite routine algebra or definitions universally. Do not use a fixed number of papers or require every sentence to have a citation.

1. State the candidate result with its full hypotheses and quantifiers, including field/characteristic, dimension, topology, regularity, category, parameter regimes, boundary assumptions, and strength of conclusion.
2. Search by theorem name, equivalent formulations, structural keywords, defining objects, natural special cases, stronger results, and citation chains. Prioritize original versions and source theorem statements; look beyond title matches.
3. Compare source and candidate claim on both assumptions and conclusion. A stronger *assumption* is not a stronger *theorem*; examine implications precisely. Record differences in generality, exceptional cases, and definitions.
4. Distinguish statement priority from method priority. An alternative proof of a known theorem is not a new theorem. A method borrowed from previous work deserves separate credit when established.
5. Identify the earliest demonstrably relevant source where feasible, but do not invent a single original discoverer when priority is unclear or dispersed among variants, unpublished preprints, or independent discoveries.
6. Decide wording and citation position in prose, then verify the `.bib` record. Where documentation is missing, mark an attribution blocker rather than inventing a record.

## Prior-art status (separate from proof validity)

- `PREVIOUSLY_KNOWN`: source contains same or mathematically equivalent conclusion under the same or weaker hypotheses; attribute clearly.
- `KNOWN_COROLLARY`: claim follows rigorously from a cited source with an explicit short deduction; attribute parent theorem.
- `ALTERNATIVE_PROOF_OF_KNOWN_RESULT`: result was known and manuscript provides a different proof; source must be cited. Say "alternative" based on actual differences; say "new proof" only with sufficient comparison of prior proofs.
- `GENERALIZATION`: manuscript claims a strictly broader result; demonstrate precisely how the earlier result is subsumed and cite it.
- `POTENTIALLY_NEW`: relevant search found no equivalence; provisional, never itself proof of novelty.
- `UNRESOLVED`: insufficient source access, unclear comparisons, or inconclusive priority evidence. Novelty claims are blocked.

## Citation placement patterns

These are *templates* only; use verified source keys and locations, not fictional metadata:

- Known theorem and self-contained proof: "The following theorem is due to [authors] [citation]. We reproduce a proof for completeness." Place the citation just before or at the theorem, not only in Related Work.
- Different proof: "[Authors] proved [statement] [citation]. We give an alternative proof based on [precise distinction, if demonstrable]." Do not characterize it as an original theorem.
- Consequence: "The next corollary follows from [theorem citation] after verifying [assumption]."
- Extension: "Theorem X extends [earlier result citation] from [setting] to [setting], subject to [precise caveat]."
- Adapted method: "We adapt the argument of [citation], replacing [technique] by [technical change]." Only if the route actually derives from that method.

A single well-placed source citation can cover a theorem and its full reproof; it need not be repeated beside each calculation. Ensure historical context in Introduction and local attribution at the result when both materially help the reader.

## Novelty statements

Avoid unsupported "the first", "for the first time", "previously unknown", "we discover", and "to our knowledge" formulas. If evidence supports a carefully scoped claim, explicitly specify the mathematical class and literature coverage; acknowledge limitations. A negative search result cannot establish that a theorem is new.

## Conflict of claim provenance and paper positioning

If the manuscript labels a known result as the paper's original contribution, correct the classification in the prose and audit. The user may still publish a useful expository or alternative-proof paper, but novelty must be honestly described. Do not silently remove the known result or fabricate a different new theorem.
