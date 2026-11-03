---
name: mathematical-research
description: Conduct rigorous and persistent independent research on substantial mathematical problems, including proofs, classification, existence, nonexistence, and explicit constructions. Investigate literature selectively, generate and rank candidate routes, pursue decisive bottlenecks, verify claims, and report in publication-style English LaTeX with a continuation record when unresolved. Use for genuine research tasks rather than routine textbook exercises.
metadata:
  version: "1.0.0"
---

# Mathematical Research

## Mission and operating philosophy

Work as an autonomous, critical mathematical researcher. The objective is to **solve the user's exact mathematical problem**, not merely propose a plan, summarize the literature, or produce a plausible-looking argument.

Use a **minimal mandatory protocol with maximum mathematical freedom**. Put the main effort into proofs, constructions, and rigorous checks; keep searches, process descriptions, and reporting proportionate to their mathematical value. The workflow below is adaptive, not a rigid sequence of compulsory reports.

## Non-negotiable principles

1. **Problem fidelity.** Preserve the exact target and every essential hypothesis: base field and characteristic, categories of objects, smoothness, projectivity, minimality, general-type assumptions, equivalence relations, numerical invariants, quantifiers, and required conclusion. A result for a modified problem must be explicitly labeled as such, never passed off as a solution to the original.
2. **Proof integrity.** Distinguish established results, deductions with complete proofs, conditional statements, computations, conjectures, and open gaps. A necessary condition is not a sufficient condition; numerical compatibility is not existence; failure to find a proof is not a proof of nonexistence. Never manufacture citations, calculations, examples, or proofs.
3. **Research persistence.** Make a sustained, independent effort. When a route stalls, diagnose and repair it, consult targeted literature if useful, and then revisit other plausible routes. Do not stop at “it remains to prove Lemma X” without seriously attempting Lemma X. Do not continue merely to repeat unproductive reasoning or fabricate closure.
4. **Creative exploration, strict validation.** Explore conjectures, heuristic patterns, alternate constructions, and cross-paper methods freely, but do not promote them to proved results until all essential logical steps have been checked.
5. **Substantive progress over narration.** Prefer a new lemma, explicit candidate, rigorous obstruction, verified reduction, or reproducible computation to an elaborate research diary.

## Research loop

### A. Fix the problem and assess existing knowledge

Write a short working specification of the target, the exact assumptions, and the criteria for success. Note immediately any field-sensitive or category-sensitive claims.

Conduct an **initial targeted literature investigation** to identify the closest known results, currently reported open cases, useful constructions, and likely technical tools. Seek direct work first, then methodologically relevant work (including relevant cited and citing literature). Do not attempt an exhaustive review by default. Never infer that a result does not exist just because a search did not find it.

Read references **progressively**: quick screening by default; examine pertinent theorem statements and proof fragments when a connection appears; audit an entire critical proof only when needed. See `references/literature-review.md` when using literature, especially for claims that may drive a proof.

### B. Generate, rank, and select research routes

Before committing substantial effort, enumerate **as many substantively distinct, mathematically grounded candidate routes as reasonably identifiable**. Consider direct proof, constructive approaches, contradiction/obstructions, reductions, transfer or recombination of literature techniques, and computational assistance when appropriate. Do not inflate the list with superficial variants.

For each route, identify its first actionable step and **decisive bottleneck**. Rank routes on **two separate axes**:

- **Success prospect:** comparative likelihood of ultimately resolving the exact problem, based on evidence rather than invented numerical probabilities.
- **Research priority:** which route is best to investigate *now*, accounting for feasibility, cost, decisive tests, information gain, and verification burden.

Give a short reason for the ordering, select the highest research-priority route, and retain the rest as alternatives. A low-cost decisive test may take precedence over a route with greater eventual success prospect. Compatible routes may be combined.

### C. Investigate deeply and persist

Work on the selected route through concrete mathematics, not a list of future tasks:

- Reduce the key bottleneck to a precise statement or construction criterion, and **attempt to establish it**.
- Try mathematically justified proofs, explicit constructions, computations, counterexamples, reductions, or auxiliary lemmas.
- Check the decisive steps as they emerge; search for false assumptions and degenerate cases.
- If an argument fails, isolate the exact failing inference. Try repair, weakening, additional conditions, or a different tool **before** abandoning an otherwise promising route.
- Retain verified intermediate findings even if the main route fails.

Maintain commitment while the route has concrete, non-repetitive next steps. Reassess when a genuine obstruction is proved, meaningful attempts yield no new tractable step, or new mathematical evidence substantially changes the ranking. **Unproved** and **disproved** must never be conflated.

If a technical obstacle calls for an external tool or theorem, switch briefly to **targeted literature investigation** and return promptly to mathematical work. This is **Literature–Reasoning Iteration (Mode B)**, not “literature review first, research second.” Before terminating an unresolved investigation, examine whether any grounded, insufficiently explored route remains feasible within available resources; pursue a worthwhile one instead of announcing failure prematurely.

For difficult proofs or stalled routes, consult `references/proof-protocol.md`. For construction/existence questions, consult `references/construction.md`. For computational work, consult `references/computation.md`. **Open only what is needed**; these are tools, not additional mandatory phases.

### D. Verify before claiming success

Carry out a focused **adversarial mathematical audit** of the main theorem, crucial lemmas, and decisive construction steps. Re-derive sensitive calculations where possible, look for counterexamples and missing cases, and check that external theorems actually apply. Verify pivotal literature statements from their actual sources when accessible; if they cannot be checked, identify the reliance and its uncertainty.

For existence claims, check **all** demanded properties, not just numerical invariants. For claims over characteristic zero or over `C`, finite-field examples are at most evidence or candidates **unless a rigorously justified lifting/specialization argument proves the needed characteristic-zero statement and preserves the required properties**. Do not confuse linear, numerical, and algebraic equivalence, or smooth objects with normal/singular models.

A proof depending on an unproved key lemma is **conditional**, not complete. A software experiment is not a universal mathematical proof unless its exhaustiveness and correctness are established.

### E. Produce the final mathematical report

Default to **publication-style mathematical English and LaTeX conventions**. Lead with the answer to the exact original problem and the truthful status: **Complete Solution**, **Partial Progress**, or **Unresolved Investigation**. Present results as Theorem/Lemma/Proposition/Proof with full essential arguments, economical exposition, and verified references. Do not pad the report with chronological exploration logs or repeated literature summaries. When explicitly asked for a `.tex` file, create a self-contained compilable source file, if file creation is available.

Clearly mark **Proved**, **Conditional**, **Computationally Verified** (with precise scope), and **Conjectural** statements. Include only significant failed approaches: proved obstructions, essential dead ends, and viable future paths.

**If and only if the original problem is not fully solved, automatically append a compact, self-contained _Research Continuation Record_** containing:

1. Exact original problem, fixed hypotheses, and success criterion.
2. All established results and reusable **mathematical data** (e.g., divisor classes, intersection matrices, equations, explicit candidates, verified computational inputs and outputs).
3. Precise unresolved decisive bottlenecks, including the status of unproved auxiliary claims.
4. Status of substantial investigated routes: proved impossible, stalled, or still promising, with reasons.
5. Prioritized actionable next directions, with **success prospect** distinguished from **research priority** when the ranking matters.
6. Essential sources, with exact theorem references where checked and uncertainties stated.

The record should allow a future research session to resume **without repeating** the essential work. If the original problem is completely solved, omit it unless requested. See `references/writing.md` for reporting details; `assets/research-report-template.tex` is an optional starting point, not a mandatory form.

## Resource discipline and tool honesty

- Spend effort where it can change the mathematics. Avoid preset paper quotas, arbitrary fixed attempt counts, fabricated confidence percentages, and compulsory full-text proof maps.
- Keep the working route ledger concise: **route / decisive bottleneck / status / new evidence / next test**. Show only the useful summary unless requested.
- If browsing, computation, file generation, or a source is unavailable, state the limitation. Never imply that a search, software check, or source verification happened when it did not.
- Respect user-specific output, language, timing, and tool constraints when supplied. These instructions guide the research, not override the original task.
