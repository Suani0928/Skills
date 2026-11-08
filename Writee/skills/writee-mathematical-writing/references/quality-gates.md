# Writee manuscript quality gates

These are substantive tests, not ceremonial checklists. Run them adaptively: local prose edits need local checks; full-paper claims need a manuscript-wide audit.

## Gate A — Mathematical fidelity

- Does each theorem match the evidence supplied by Researchee or the author, including exact assumptions, quantifiers, field/characteristic, regularity, and conclusion?
- Are proof dependencies legitimate and noncircular? Are nontrivial steps justified rather than hidden by "standard", "clearly", or "similarly"?
- Are conditional, computational, conjectural, open and refuted results labeled truthfully?
- Has editorial restructuring introduced a mathematical difference? If so, prove equivalence or record the change explicitly.

**Blocker**: a critical missing lemma, a false implication, an unsupported stronger conclusion, or changed hypotheses without justification. Correct when possible; otherwise downgrade result and refer the exact issue to research.

## Gate B — Mandatory prior-art attribution

- Has each substantial principal result received appropriately targeted known-work screening?
- If an identical or equivalent known result exists, is it clearly identified as *known*, with a citation in the body **even if the paper supplies its own complete proof**?
- For the theorem's published source, is a corresponding verified record in `.bib`? For a known corollary, is the parent theorem correctly credited?
- If an alternative proof is offered, is the novelty of the proof distinguished from priority of the result? Is the claim that a proof is new defensible?
- Are prior generalizations/methods credited, and are statements of originality/firstness consistent with actual evidence?

**Blocker**: a known result presented as new, missing attribution, fictional bibliography, or unsupported priority/novelty claim.

## Gate C — Citation reliability

- Are quoted bibliographic facts authentic? Are pivotal imported theorems checked against actual source statements and hypotheses (`L3` where feasible)?
- Do citations make mathematically true implications, not merely support vaguely related topics?
- Are theorem locators and versions verified? Are unresolved claims explicitly labeled rather than covered by a confident `\cite`?
- Does every live `\cite{...}` map to a legitimate `.bib` entry, and do attribution claims appear in the text rather than only in the bibliography?

**Blocker**: invented metadata or unverified but essential source presented as checked. For inaccessible primary material, mark verification incomplete and limit finalization claims.

## Gate D — Manuscript coherence and style

- Do abstract, Introduction, theorem statements and conclusion claim the same scope and novelty status?
- Are symbols, references, section order, definitions, and theorem numbering coherent throughout?
- Does the requested paper/author reference only guide high-level exposition, without textual replication or inappropriate reference transfer?
- Is proof length and mathematical motivation appropriate for the intended audience? Do technical details remain visible where needed?

## Exit states

`READY_FOR_AUTHOR_REVIEW`: No known critical proof/fidelity or citation blockers within performed review; not a guarantee of acceptance or formal verification.

`DRAFT_WITH_BLOCKERS`: Substantial mathematical issue, missing crucial source, attribution ambiguity, or incomplete bibliographic verification. Deliver the draft if useful, with exact blockers and no publication-readiness claim.

`RESEARCH_RETURN_REQUIRED`: A core lemma/proof remains uncertain and requires substantive research. Give a precise return task for Researchee or equivalent research workflow.

## Compact audit structure

```
Manuscript state: <exit state>
Mathematics: <what was examined; unresolved gaps>
Prior art: <principal claims; classification; known results and citations>
Citations: <what actual sources were inspected; verification levels; missing entries>
Style: <examples read and high-level traits adopted, or access limitation>
Editorial changes: <meaningful modifications and justification>
Tool limitations: <e.g., no PDF/full-text access or no LaTeX compilation>
```

Do not misreport a model's self-check as independent professional peer review, or a role-based prompt as a genuinely separate agent. Prefer specific evidence and minimal noise.
