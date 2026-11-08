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

## Plugins

This repository includes complete source snapshots of two installed plugins:

| Directory | Plugin version | Plugin identifier | Purpose |
| --- | --- | --- | --- |
| [`Researchee/`](Researchee/) | `2.5.0` | `mathematical-research` | Mathematical discovery, proofs, constructions, and research records |
| [`Writee/`](Writee/) | `0.1.0` | `writee` | Mathematical manuscript writing, prior-art attribution, and citation review |

### Researchee

Start with a mathematical problem, its hypotheses, and any existing results. Researchee investigates possible approaches, develops proofs or constructions, checks arguments, and records what has been established and what remains unresolved. Manuscript preparation belongs to Writee.

Entry point: [`Researchee/skills/mathematical-research/SKILL.md`](Researchee/skills/mathematical-research/SKILL.md).

### Writee

Start with research results, proofs, a draft manuscript, or reference papers. Writee develops and revises mathematical prose, checks attribution of known results, reviews citations, and organizes LaTeX manuscripts. A full-paper delivery normally includes `main.tex`, `references.bib`, and `writing-audit.md`; the supplied templates are starting points to be completed for each project.

Entry point: [`Writee/skills/writee-mathematical-writing/SKILL.md`](Writee/skills/writee-mathematical-writing/SKILL.md).

The plugins can be used independently. For a research-to-writing workflow, pass Researchee's results, proofs, unresolved issues, and source records to Writee. The [handoff guidance](Researchee/skills/mathematical-research/references/writee-handoff.md) and [optional YAML template](Writee/skills/writee-mathematical-writing/templates/research-handoff.yaml) describe this exchange; they do not implement automatic calls between the plugins.

## Legacy skill

The earlier standalone `math-researchen/` skill remains in repository history and the committed tree for continuity. Use the plugin release directories above for the imported releases.

### `math-researchen`

A rigorous mathematical research workflow for investigating difficult problems, developing proofs, exploring constructions, and producing research-quality reports.

Its core principles include:

- **Literature–reasoning iteration:** begin with targeted literature research, then alternate mathematical reasoning and further reading as concrete obstacles arise.
- **Research-route selection:** identify substantively different approaches, rank them by success prospects and immediate research priority, and choose an approach for sustained investigation.
- **Deep investigation and persistence:** actively work on decisive lemmas and constructions, repair failed arguments, and reassess alternative routes rather than stopping at a research plan.
- **Mathematical integrity:** preserve the original problem and its hypotheses; distinguish rigorous proofs from conjectures, computational evidence, and conditional conclusions.
- **Result-oriented reporting:** default to publication-style mathematical English and LaTeX; when the problem remains unresolved, include a compact **Research Continuation Record** with precise obstacles, reusable results, and prioritized next steps.

The skill is domain-general, with optional guidance for algebraic-geometric constructions, computational experimentation, literature analysis, proof verification, and mathematical writing.

## Repository organization

The imported plugins retain all their original files, including hidden compatibility manifests:

```text
Researchee/
├── plugin.json
├── .codex-plugin/plugin.json
└── skills/mathematical-research/
    ├── SKILL.md
    ├── assets/
    └── references/
Writee/
├── plugin.json
├── .codex-plugin/plugin.json
└── skills/writee-mathematical-writing/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── templates/
```

`Researchee/` and `Writee/` are repository directory names. Their original plugin identifiers and internal paths have been preserved. Plugin release versions come from the manifests; Researchee's skill-level `metadata.version` remains `1.0.0` as supplied and is separate from its plugin version.

The legacy standalone skill uses this layout:

```text
<skill-name>/
├── SKILL.md                 # Entry point and core behavioral instructions
├── references/              # Detailed, selectively loaded guidance
├── assets/                  # Templates or other supporting files
└── README.md                # Skill-specific documentation (optional)
```

`SKILL.md` is the primary source of instructions. Supporting materials should remain modular so that a skill need not load every reference for every task. Individual skills may have fewer or different files depending on their needs.

## Usage

1. Choose `Researchee/` or `Writee/` and read the linked `SKILL.md`.
2. Keep the complete plugin directory together, including `plugin.json`, `.codex-plugin/`, and `skills/`. The imported releases contain 10 and 15 files respectively.
3. Follow the installation instructions of a host that supports the package format. Cloning the repository alone does not activate either plugin.
4. If using a skill independently, retain its supporting references, templates, assets, and agent metadata.

For an upload that accepts plugin archives, package each plugin separately, with its `plugin.json` at the archive root or in the single enclosing plugin directory. Include hidden files. Do not package the entire repository as one plugin.

Some ChatGPT environments support private plugins containing skills. A skill directory by itself is **not** necessarily an installable plugin: plugin packaging may require a separate manifest and compatible directory layout.

## Source integrity

These snapshots preserve the installed source files without modifying their manifests, instructions, or templates. They contain no MCP server configuration or bundled service credentials. Author names and contact emails remain in the original manifests. Static file checks do not establish runtime behavior or mathematical correctness.

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
