# Research Skills

A personal collection of reusable AI skills developed through iterative collaboration with ChatGPT.

The goal of this repository is to turn carefully considered working preferences into portable, inspectable instructions—not to accumulate elaborate prompts. Each skill is designed for a specific workflow, with a concise core protocol and additional references only where they are useful.

## Philosophy

The skills in this repository follow a few shared principles:

- **Substance over ceremony.** Instructions should help the model do the work, not spend its effort describing a workflow.
- **Autonomy with accountability.** Encourage independent exploration while maintaining clear standards for verification and reporting.
- **Adaptive rather than mechanical.** Use tools, references, and intermediate checks when they improve the task; avoid mandatory steps without a purpose.
- **Traceable results.** Distinguish established findings from hypotheses, experiments, and unfinished work.
- **Iterative improvement.** Revise skills in light of actual use, observed failure modes, and new requirements.

## Skills

### `math-researchen`

A rigorous mathematical research workflow for investigating difficult problems, developing proofs, exploring constructions, and producing research-quality reports.

Its core principles include:

- **Literature–reasoning iteration:** begin with targeted literature research, then alternate mathematical reasoning and further reading as concrete obstacles arise.
- **Research-route selection:** identify substantively different approaches, rank them by success prospects and immediate research priority, and choose an approach for sustained investigation.
- **Deep investigation and persistence:** actively work on decisive lemmas and constructions, repair failed arguments, and reassess alternative routes rather than stopping at a research plan.
- **Mathematical integrity:** preserve the original problem and its hypotheses; distinguish rigorous proofs from conjectures, computational evidence, and conditional conclusions.
- **Result-oriented reporting:** default to publication-style mathematical English and LaTeX; when the problem remains unresolved, include a compact **Research Continuation Record** with precise obstacles, reusable results, and prioritized next steps.

The skill is domain-general, with optional guidance for algebraic-geometric constructions, computational experimentation, literature analysis, proof verification, and mathematical writing.

> **Note:** Additional skills will be documented here as they are added. This list intentionally includes only skills confirmed to be part of the collection.

## Repository organization

A typical skill in this repository may use the following structure:

```text
<skill-name>/
├── SKILL.md                 # Entry point and core behavioral instructions
├── references/              # Detailed, selectively loaded guidance
├── assets/                  # Templates or other supporting files
└── README.md                # Skill-specific documentation (optional)
```

`SKILL.md` is the primary source of instructions. Supporting materials should remain modular so that a skill need not load every reference for every task. Individual skills may have fewer or different files depending on their needs.

## Usage

1. Open the directory of the skill you want to use and read its `SKILL.md`.
2. Use the skill in an AI environment that supports skill files, or adapt the core instructions to that environment's custom-instruction mechanism.
3. Keep referenced files with the skill so its instructions remain complete.
4. Follow any skill-specific setup notes; packaging and installation vary by platform.

Some ChatGPT environments support private plugins containing skills. A skill directory by itself is **not** necessarily an installable plugin: plugin packaging may require a separate manifest and compatible directory layout.

## Development guidelines

When creating or revising a skill:

1. Define the task, intended use cases, and non-negotiable constraints.
2. Keep the main `SKILL.md` focused on the decisions and behaviors that actually matter.
3. Move detailed or specialized procedures into optional references.
4. Test against realistic tasks, particularly cases where previous model behavior was unsatisfactory.
5. Update instructions based on observed results rather than increasing complexity by default.

## Status

This is an evolving personal collection. The skills are working research and productivity tools, not guarantees of correctness or complete solutions. Mathematical claims, citations, code, and other consequential outputs should be independently verified where appropriate.

## License

No license has been specified yet. See the repository's `LICENSE` file if one is added later.
