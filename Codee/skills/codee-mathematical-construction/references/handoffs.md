# Optional Researchee / Writee compatibility (no automatic link)

Codee is **standalone**. Source can be user-uploaded paper or a pasted/attached research handoff. Use provenance as data, never as verified proof. Do **not** claim that Codee can read another plugin's conversation, execute it, write into it, or call its internal tools without a genuinely connected integration.

## Researchee → Codee
The user's installed Researchee (mathematical-research) reports Complete Solution / Partial Progress / Unresolved Investigation and may supply a Research Continuation Record or a `Research Handoff` with headings:
- Original problem and exact scope/assumptions;
- Established claims with proofs, dependencies and source attribution;
- Conditional or conjectural claims;
- Computational/construction evidence (formulae, scripts, exact examples);
- Mathematical source provenance and unresolved gaps.

Accept prose, Markdown, LaTeX or structured YAML/JSON; no mandatory schema. Transform into MCR claim ledger, preserve origin and proof-status distinctions. Never upgrade `claimed proved`, `from report`, or `implemented` to `independently verified`. A missing full definition or proof stays `UNKNOWN` or blocked, not invented.

## Writee → Codee
Writee can produce a full LaTeX manuscript, PDF or Markdown with definitions, lemmas, calculations and equations. Locate the *exact* mathematical target and formula/section labels; take manuscript status (`draft`, `claimed theorem`, etc.) as evidence of authorial intent, not correctness. The installed Writee has an **optional** `writee-handoff/1.0` intake packet (it describes research provenance, not a Codee endpoint) with `research`, `claims`, `proof_dependencies`, `related_literature`, `known_gaps`, `style_references`. If supplied, import mathematical claims and dependencies only, preserve citation/provenance, and ignore stylistic preferences unless user explicitly asks for code documentation tone. Accept raw `.tex` by default.

## Codee → Researchee
For independent further research, produce a precise `Codee Research Feedback` containing: target theorem, first unsupported claim, proven partial lemmas, exact counter-witness if found, candidate mathematical repair clearly marked, computational artifacts, source anchors, prerequisites and how to reproduce. This is transferable text or a file, not an automatic plugin-to-plugin message.

## Codee → Writee
Produce a `Codee Computation Handoff`: claim-level verification status, source-to-code mapping, mathematical statement and theorem premises, executed software versions and command, exact result/witness, independent checker status, unverified hypotheses, and verified citations where actual sources were accessed. Writee can use it to write code methods/appendix and cite software or mathematical theorems; do not generate fabricated citations, publication-ready prose or claim original priority.

## Suggested minimal packet
```
protocol: codee-handoff/1.0
origin: user | researchee | writee | external
source_artifacts: []
claims:
  - id: C1
    statement_latex: ...
    hypotheses: []
    dependencies: []
    source_refs: []
    origin_proof_status: UNKNOWN
    codee_fidelity_status: UNCHECKED
    codee_mathematical_status: NOT_RUN
computation_targets: []
```
This is only a suggested metadata packet; ordinary reports and manuscripts remain supported.
