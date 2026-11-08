# Mathematical manuscript architecture and writing

## Aim

Create a mathematical argument at manuscript scale: not just grammatically correct English, but a coherent path from problem motivation to exact theorems, proofs, technical contributions, and accurately attributed existing work.

## Before drafting

- Extract the research's *proven* core: what has been established, under which assumptions, and with what dependencies. Separate independently interesting statements from auxiliary results.
- Identify the audience, venue, level of background, and preferred length if the user supplies them. Otherwise use a clear research-mathematics register with compact exposition and necessary proof detail.
- Map the mathematical story: the central difficulty; established related results; the new/alternative/expository contribution; the strongest justified statement; what is deliberately not claimed.
- Organize main theorems in a reader-friendly sequence that respects logical dependencies. Consider moving long technical lemmas to preliminaries or appendices only when that helps comprehension.
- Run prior-art screening *before* claiming a result as a contribution. A fully proved familiar result may be a useful part of a paper but should never be presented as newly discovered.

## Section responsibilities

**Title and abstract:** only assert results in the checked research corpus; do not claim firstness or a generalization that the comparison audit cannot support. Abstract may briefly acknowledge a substantially known central theorem if the paper is about its proof or exposition.

**Introduction:** explain motivation, natural mathematical objects, established background with supported references, exact questions, carefully scoped contribution, relationship to closest work, and a roadmap if useful. Avoid unsupported claims about the literature. Introductory summaries must match actual theorem statements.

**Related work:** may be a distinct section or integrated in Introduction depending on conventions. Separate earlier theorem statements, method sources, adjacent questions, and conceptual analogies. Cite primary and secondary material appropriately; don't transfer citations from a style exemplar unless relevant and verified.

**Preliminaries:** state notation, definitions, and nonstandard conventions before use; cite imported technical tools with exact applicability and conditions. Avoid reintroducing incompatible notation.

**Main results:** clear hypotheses and quantifiers; sensible theorem/proposition/lemma hierarchy. State comparisons to known results precisely and give direct attribution near known results, even for full reproofs.

**Proofs:** start with the goal and meaningful strategy when useful; expose nontrivial logical transitions and verify external lemmas. Preserve meaning under editorial compression, including uniformity, measurability, exceptional sets, quantifiers, or characteristic issues.

**Conclusion/discussion (only if natural):** discuss scope, established consequences, limitations, and explicit open questions; avoid manufactured impact statements.

## Editorial mathematical reasoning

Writee may:
- split an established proof into well-justified lemmas;
- supply routine missing algebra/analytic details and verify them;
- present an equivalent theorem statement after checking equivalence, while recording the change;
- reorder results to improve narrative, keeping definitions and dependencies valid;
- suggest more natural positioning of examples and remarks.

Writee must not:
- silently strengthen theorems, alter hypotheses, change equivalence relations, or conflate proven/conditional statements;
- create new technical claims simply to bridge prose;
- call an incomplete proof complete;
- claim novelty based on proof reconstruction;
- start an extensive fresh research project behind the user's back.

If a proof is fundamentally missing, draft an accurate statement of the bottleneck and hand it back to the research workflow. For partial results, prefer honest formulations such as conditional theorems, propositions with explicit additional hypotheses, or exploratory notes—never fiction.

## Style and citations

The user's chosen reference papers inform broad exposition traits; apply section-specific analysis from `style-analysis.md`. Accuracy and mandatory attribution remain fixed. If the style model is very sparse in citations, Writee must still cite known results and method origins appropriately.

## Manuscript deliverables

When only a subsection is requested, supply that subsection and a concise note of unsolved citation or mathematics issues. For a whole manuscript, prioritize a coherent `main.tex` and a matching `references.bib`, then a compact `writing-audit.md`. If asked for a particular LaTeX class/journal template, follow its requirements; otherwise use standard `amsmath`, `amsthm`, and `amssymb` conventions. Validate cross-references and compilation when a compiler is actually available; otherwise say compilation was not run.
