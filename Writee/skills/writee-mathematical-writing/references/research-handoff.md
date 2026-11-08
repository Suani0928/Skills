# Research handoff: Researchee → Writee

## Purpose and trust model

Use a finished Researchee report, a partial investigation with its Research Continuation Record, or user-provided notes/proofs as *source material* for writing, not as proof of external verification or originality. The same protocol applies if Researchee is absent. The user may paste a report, upload `.tex`, or provide an equivalent research summary. No direct cross-plugin API is assumed.

Researchee's established reporting conventions include Complete Solution / Partial Progress / Unresolved Investigation; theorem/proof text and exact hypotheses; checked or unchecked literature; and, when work is incomplete, a Research Continuation Record. Ingest all of these as available. A complete solution need not have a continuation record.

## Minimum manuscript intake

1. Original target and exact hypotheses, including base field, objects, ambient category, quantifiers, regularity, exceptional cases.
2. Statements and labels of results claimed proved, conditional, computational, refuted, or unresolved.
3. Full arguments or sufficient mathematical evidence for the result(s) to be written. Do not upgrade a bare assertion of success to a verified proof.
4. Claim dependencies and externally imported results, including what version or theorem in the source was used if known.
5. Existing bibliographic citations, with source-verification status clearly distinguished from mere metadata.
6. User's intended contribution, audience, journal/section, authorial preferences, and style references if specified.

If a key item is missing, work from what is available and identify the missing material precisely. Do not ask for all items by default. If the missing item prevents a formal theorem/proof from being written, prepare a labeled draft and state the blocker.

## Internal claim/provenance ledger

Maintain compact rows, internal by default:

`claim_id | exact statement | origin (user/Researchee/source/Writee deduction) | proof_status | prior_art_status | source_ids | dependencies | editorial_risk`

- `proof_status`: `PROVED_IN_SUBMITTED_MATERIAL`, `LOCALLY_CHECKED`, `CONDITIONAL`, `INCOMPLETE`, `REFUTED`, `COMPUTATIONAL_ONLY`, `UNKNOWN`. The first label never implies independent verification.
- `prior_art_status`: `PREVIOUSLY_KNOWN`, `KNOWN_COROLLARY`, `ALTERNATIVE_PROOF_OF_KNOWN_RESULT`, `GENERALIZATION`, `POTENTIALLY_NEW`, `UNRESOLVED`. This axis must remain independent of proof status.
- `origin` indicates where this manuscript input came from; it does **not** establish original academic priority.

For an unsolved or conditional Researchee report, treat the continuation record as research context. Do not falsely turn stalled routes or necessary conditions into complete results.

## Optional proposed machine-readable packet

This is a **format suggestion**, not a real plugin-to-plugin endpoint or a required input. It may be constructed by Writee from ordinary reports:

```yaml
protocol: writee-handoff/1.0
research:
  source: user-supplied-research-report
  outcome: partial  # complete | partial | unresolved
claims:
  - id: C1
    statement_latex: "..."
    hypotheses: []
    proof_status: PROVED_IN_SUBMITTED_MATERIAL
    proof_latex: "..."
    dependencies: []
    literature_sources: []
open_problems: []
style_references: []
```

## Boundary handling

- Writee may reorganize proofs, add justified intermediate details, and check implications *for exposition fidelity*.
- If a serious logical gap arises, isolate the smallest exact missing assertion and label the result conditional or incomplete as appropriate. Suggest returning it to Researchee, with the precise statement and context.
- Writee never needs to rewrite Researchee configuration or assume its tools are available.
- Prior-art investigation begins **after** ingestion and is independent of Researchee's research-route literature search. A known theorem **must still be cited even when the submitted proof is self-contained**.
