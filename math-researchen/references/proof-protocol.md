# Deep mathematical investigation and proof audit — on-demand guide

Use this guide when a decisive lemma is difficult, a route stalls, or a major result is ready for verification. **Do not turn the guide into a narrated checklist.**

## Attack the decisive bottleneck

State the necessary intermediate claim precisely, with quantifiers and assumptions. Check whether it is true in extreme, low-dimensional, singular, or characteristic-dependent cases. Ask whether a counterexample can be built before investing heavily in a proof.

Attempt a substantive argument. Depending on the problem, try direct calculation, auxiliary objects, induction, deformation, degeneration, contradiction, invariants, duality, symmetry, or reduction to a known theorem. These are options, not required steps. When an intermediate lemma is proposed, **attempt to prove it**, not merely place it in a plan.

For an unsuccessful attempt, isolate the smallest unproved or false assertion. Seek a repair, weaker conclusion, sufficient additional condition, or alternate route. A failure to prove a statement must not be reported as a disproof.

## Route status

Use only meaningful distinctions:

- **Established:** A complete proof or fully justified construction exists.
- **Conditional:** A result follows if an explicitly stated unproved hypothesis holds.
- **Open bottleneck:** A precise question remains; no proof or counterexample established.
- **Disproved:** A correct counterexample refutes an intermediate claim, or an impossibility proof rules out the route.
- **Dormant:** Attempts yielded no tractable next step; another route currently has higher research priority.

Maintain the minimal working ledger `route | bottleneck | status | evidence | next decisive test`. Rerank only for mathematically substantive reasons. Do not repeat failed attempts without changing an assumption, tool, or construction.

## Adversarial final audit

Focus scrutiny on steps that could invalidate the main conclusion:

- Confirm exact match with the original problem and all hypotheses.
- Trace every nontrivial inference to a valid proof, calculation, or correctly applicable theorem; flag circular dependencies.
- Separate existence from parameter-counting or numerical consistency, and necessary from sufficient conditions.
- Probe boundary and degenerate cases, unintended extra components, singularities, and any special-vs-general claims.
- Check field/characteristic, equivalence relations, and the passage between a model and its normalization, resolution, contraction, or minimal model.
- Recompute sensitive identities independently when feasible. If an argument needs a missing lemma, downgrade the conclusion to **conditional**.

A strong audit is concentrated and evidence-based, not a ceremonial claim that everything has been checked.
