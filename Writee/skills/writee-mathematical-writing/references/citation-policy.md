# Research-grade citation and evidence policy

## Nonnegotiable contract

Every substantive claim taken from or already established in the literature must be properly attributed when the source can be established. In particular, the author of a newly *written* proof of an already *known* result is **not** the originator of the theorem. Cite its known source in the body and include that source in the bibliography. When source discovery or verification is blocked, leave an explicit high-priority action item; do not fabricate the missing paper or promote an uncited known result as original.

A citation has two distinct dimensions:

- **Bibliographic validity**: actual identity of article/book/preprint, author list, title, year, venue, DOI or arXiv identifier, and version where relevant.
- **Mathematical applicability**: a specifically located result actually implies the statement for which the manuscript cites it, including imported assumptions and relevant version of source definitions.

Crossref/DOI metadata alone establishes neither a theorem nor an exact theorem number. A search snippet or citation found in a different paper is a lead, not direct verification.

## Evidence levels

- `L0 CANDIDATE`: apparent lead, metadata not confirmed. Never use as a definitive source in the manuscript.
- `L1 METADATA_VERIFIED`: record confirmed through reliable bibliographic metadata; mathematical claim not checked.
- `L2 SOURCE_LOCATED`: source and relevant passage located, but mathematical applicability not fully checked.
- `L3 CLAIM_VERIFIED`: actual source statement, version/location, relevant hypotheses and conclusion inspected; the cited use is justified, or a gap is explicitly marked.

Aim for `L3` on all **pivotal imported theorems**, claims of equivalence to previously known results, and precision-dependent novelty comparisons. For contextual history or general background, `L1` plus trustworthy support for the historical claim may suffice; strive for direct primary evidence when contested. Do not mark a Level 3 claim merely because the source is reputable. Report when access or verification is limited.

## Claim-to-source ledger

For each significant source-supported claim record:

`claim_id | manuscript location | citation_key | bibliographic_verified? | actual_source_url_or_identifier | source_version | theorem/page/section | source_hypotheses | comparison_to_claim | evidence_level | unverified_items`

For unattributed known results record the claim with `citation_key=null`, `status=ATTRIBUTION_BLOCKER`, and an actionable search step. Do not supply a fake key.

Use enough granularity to identify the mathematical risk. A list of BibTeX entries alone is not an attribution audit.

## Literature strategy for manuscripts

1. Collect sources from the research handoff, inspect actual cited statements if reachable, and recheck any bibliographic uncertainties.
2. Conduct *manuscript-specific* prior-art research for main results. Researchee's targeted literature search optimized for solving the problem is not a substitute for attribution screening.
3. Conduct an appropriately scoped related-work review for Introduction. Differentiate landmark history, closest mathematical antecedents, method sources, and surveys. Prefer originals for priority; surveys can be cited for orientation when appropriate.
4. Use accessible scholarly sources, such as journal/publisher pages, author manuscripts, arXiv, DOI resolvers, Crossref, zbMATH Open, and MathSciNet when access exists. Do not claim subscription access without actual access. If multiple versions conflict, record the one checked.
5. For central cited results, check theorem wording/assumptions. Investigate adjacent definitions and theorem dependencies as necessary, rather than inferring validity from title or abstract.
6. Stop expanding the bibliography when further sources no longer materially improve attribution, claim support, or contextual accuracy. Do not pad citations with irrelevant literature.

## Citation integrity in prose

- Attribute theorem *statement priority* even with a novel or independently rediscovered proof. Attribute method provenance separately.
- Check statement vs source: mathematical fields, assumptions, regularity, orientation, parameter intervals, existence versus necessity, generic versus every, local versus global, and exact conclusion.
- Use exact theorem numbers, equation numbers, page references only when checked in the cited version. If unavailable, cite without fabricated locator and identify the limitation in the audit.
- Do not claim that a source proves a stronger assertion than it does.
- Avoid verbatim borrowing or close paraphrase of published exposition; mathematical facts can be restated independently with citation.

## Failure states and output

If evidence for a material attribution is unavailable, the text may be delivered only as a **working draft requiring verification**, with exact unresolved claims and missing source details. Do not fabricate bibliographic metadata or silently omit the citation. In LaTeX, use an explicit editorial TODO comment or prose note that does not pretend to be a complete `\cite{...}`. In the audit, note the blocker, what was checked, and a feasible next action.

Final audit must ensure all used `\cite{key}` keys exist in the `.bib` file, entries are genuine to the level described, and important known results have matching body attribution. Do not label a reference as mathematically verified merely because it has a valid DOI.
