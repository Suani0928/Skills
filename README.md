# Research Skills

Three AI plugins for mathematical research, computational verification, and manuscript writing. Use them independently or pass proofs, constructions, and source notes between them as your work develops.

## Choose a plugin

| Plugin | Version | Start with | What you get |
| --- | --- | --- | --- |
| [Researchee](Researchee/) | `2.5.0` | A problem, its hypotheses, and any partial results | Proofs, constructions, or counterexamples. For an unresolved problem, a research record with established results and open steps. |
| [Codee](Codee/) | `1.1.1` | An explicit construction, example, or algorithm | Annotated code, commands to run it, and results from checks it can perform with the available mathematical software. |
| [Writee](Writee/) | `0.1.0` | A proof, research report, or manuscript draft | LaTeX sections or a full manuscript, with checks on prior work, citations, and attribution. |

## From a research question to a manuscript

1. **Investigate with Researchee.** Give it the exact problem and hypotheses. Ask it to pursue a proof or construction and record which claims are established and which still need work. [Research skill](Researchee/skills/mathematical-research/SKILL.md)
2. **Check an explicit construction with Codee.** Pass the formulas, definitions, and specific properties you want checked. Codee reports whether the program implements the construction faithfully and which mathematical checks it ran. [Coding skill](Codee/skills/codee-mathematical-construction/SKILL.md) · [Python examples](Codee/skills/codee-mathematical-construction/examples/)
3. **Prepare the manuscript with Writee.** Pass the proofs, sources, and relevant computational results. A full manuscript can include `main.tex`, `references.bib`, and `writing-audit.md`. [Writing skill](Writee/skills/writee-mathematical-writing/SKILL.md)

Start at the step that matches the material you already have. When moving between plugins, pass the relevant files or excerpts yourself. Keep the hypotheses, source references, and limits of any computational check with the result they support. [Research-to-writing handoff](Researchee/skills/mathematical-research/references/writee-handoff.md) · [Codee handoffs](Codee/skills/codee-mathematical-construction/references/handoffs.md)

## Use the source packages

Each plugin directory is a complete source snapshot. Keep `plugin.json`, the hidden `.codex-plugin/` directory, and `skills/` together when importing the package into a compatible host. Follow that host’s installation instructions.

To read a skill on GitHub, open its `SKILL.md` from the links above. The nearby references, templates, and examples provide supporting material for specific tasks.

Versions in the table come from the plugin manifests. Codee’s bundled README still has a `v1.1.0` heading. Both of its manifests specify `1.1.1`.

## License

A license has yet to be specified for this repository.
