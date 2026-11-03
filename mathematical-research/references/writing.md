# Mathematical research reporting — on-demand guide

Default to **publication-style English with LaTeX mathematics**, even when the conversation itself is in another language. Follow the user's explicit output-format requests. When a `.tex` file is requested and tools permit, deliver a compilable source file.

## Outcome-first structure

Choose the truthful outcome: **Complete Solution**, **Partial Progress**, or **Unresolved Investigation**. Immediately specify what is and is not established concerning the **original** problem.

Present substantial results in a clean mathematical order:

- Precise assumptions and notation when needed.
- Theorem/Lemma/Proposition/Corollary, explicit constructions, and complete essential proofs.
- Precise scope and limitations of computational claims and conditional conclusions.
- Verified citations for results actually used; flag unverified bibliographic or theorem details.
- Exact remaining obstacles, but only if the target remains unresolved.

Use rigorous, economical exposition. Do not over-explain routine algebra, but never compress a hard step into “obvious,” “standard,” or “similarly” without a valid reference or sufficient argument. Do not build an impressive-looking theorem-proof structure around an unproved decisive lemma.

## Required continuation record when unresolved

Append a distinct `Research Continuation Record` section to **every** partial or unresolved final report. Make it self-contained but brief:

1. **Original problem:** Exact target, field, hypotheses, success criterion.
2. **Established results and reusable data:** Proven lemmas, formulas, divisor classes, intersection numbers, defining equations, explicit examples, exact computations, and dependencies as applicable.
3. **Unresolved bottlenecks:** State the precise unproved lemma/constructibility condition and what is already known about it.
4. **Routes investigated:** Mark each substantial route as ruled out by proof, stalled, or still viable; give the concise mathematical reason.
5. **Next research priorities:** Ranked actionable steps, not vague topics; distinguish success prospect from priority when needed.
6. **Essential references:** Sources plus exact theorem identifiers when verified; otherwise state verification limits.

Do **not** preserve a chronological transcript of guesses, failed calculations, or internal reasoning. Preserve only information useful for verification and continuation. Omit the record on a complete solution unless the user asks for it.

## LaTeX source

See `assets/research-report-template.tex` for an optional compilable skeleton. Replace all placeholders with actual supported content, and remove unused sections. The template is not a reason to pad a short result. Prefer standard `amsmath`, `amssymb`, and `amsthm` conventions and consistent notation. Do not fabricate bibliography entries or theorem numbers.
