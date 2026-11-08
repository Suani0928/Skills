# Reference-guided mathematical exposition

## Trigger

The user may say "仿照 XXX 的写作风格" or specify a mathematician, journal, paper, arXiv link, uploaded PDF/LaTeX, or multiple exemplars. This is a request for the **high-level characteristics** of mathematical exposition, not textual copying.

## Evidence-first style intake

1. Resolve the exact exemplar(s). A specific uploaded paper or URL is preferable to a vague author label; if only an author is named, use representative accessible papers where tools allow, without pretending the author's entire oeuvre is uniform.
2. Read actual accessible passages for the targeted section; if no paper can be accessed, say so and use only general traits that can be grounded. Do not fabricate a paper-specific or author-specific analysis.
3. Separate *style source* from *mathematical citation source*. A model paper is not automatically relevant to the manuscript's theorem or prior-art attribution. Never import its bibliography wholesale.
4. Extract transferable characteristics, not distinctive wording. Do not reproduce paragraphs, proof prose, or the author's idiosyncratic phrasing. For requests naming a living author, offer an original text sharing only broad qualities (e.g., concision, proof granularity, motivation density).
5. If exemplars disagree, prioritize the user's assignment per section and produce a single coherent manuscript voice.

## Style profile dimensions

- **Narrative arc:** problem history → obstruction → main contribution → mathematical implications, or alternative mathematically appropriate ordering.
- **Exposition density:** amount of motivation before definitions and theorems; whether technical context is introduced inline or in preliminaries.
- **Proof architecture:** modular lemmas versus long arguments, roadmap paragraphs, step names, how and when technical tools are introduced.
- **Theorem design:** hypotheses first versus bundled notation, how special/general cases are staged, where explanatory remarks occur.
- **Equation integration:** displayed formulas versus prose, number of intermediate steps, equation tagging and cross-references.
- **Citation rhetoric:** how the reference frames related work (but never copy a style that suppresses necessary attribution).
- **Linguistic register:** formal/concise/explanatory, active versus impersonal formulations, sentence rhythm at a broad level.

## Section-specific adaptation

- **Introduction:** research motivation and literatures may need more context than a concise proof section.
- **Main results:** state exact hypotheses, identify novelty conservatively, and present theorem relationships.
- **Proof:** preserve mathematical reasoning, use explanatory signposts only where valuable, avoid hiding hard steps behind "clearly".
- **Related Work:** attribution and comparison are evidence-driven; style cannot override citation completeness.

## User steerability

Allow requests like "same structural style, but more motivation" or "keep every proof step and reduce verbal density". Change only the relevant dimension and report material mathematical rewrites. Default to preserving the user's current voice if no exemplar is supplied. Use one or more samples to infer local conventions; do not claim a universal, objective mathematical style ranking.

## Tiny optional style profile schema

```yaml
style_profile:
  source_type: supplied_paper
  source_evidence: actually_read | partially_read | not_accessible
  narrative: concise
  proof_granularity: explicit_on_nontrivial_steps
  notation: consistent_with_user
  introduction_context: moderately_detailed
  citation_policy_override: forbidden
  no_textual_replication: true
```
