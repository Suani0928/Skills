# LaTeX, bibliographic data, and reproducibility

## Mathematical LaTeX standards

- Preserve exact mathematics and existing user macros when compatible. Respect the document class, preferred citation scheme, and journal template if supplied.
- Use `amsthm`-style theorem environments or the journal's theorem definitions; consistent numbering, labels, and `\ref`/`\eqref` references. Label a major claim once, refer to it consistently.
- Display equations only when appropriate; use explicit delimiters, clear operator notation, and unambiguous quantification. Avoid changing semantics through symbol substitution.
- Do not reorder proofs so a referenced lemma appears after it without signposting, or rename variables in ways that shadow assumptions.
- Keep explanatory text original; never copy illustrative paragraphs from style-reference papers.

## `.bib` integrity rules

- Add only real works with metadata actually supported by accessible evidence. Do not invent volume, issue, pages, publisher, DOI, arXiv ID, theorem number, or year. Omit fields not verified.
- Check the exact title, author list, year, and publication venue/version from reliable source metadata. If referring to a preprint version, preserve its version when theorem numbering differs.
- Use stable, unique, descriptive BibTeX keys; keys must match the text's `\cite{...}` uses exactly. If the user's bibliography supplies a key already in use, reuse it rather than duplicating the paper.
- Choose one bibliography system: standard BibTeX (`\bibliographystyle` / `\bibliography`) unless the user requires `biblatex` or a particular journal format. Avoid mixing their commands.
- Citation syntax: cite the earliest appropriate source of a theorem, with a theorem locator only if actually checked (for example `\cite[Theorem 3.2]{VerifiedKey}`).
- An existing known theorem with a rewritten/self-contained proof **still needs a source citation in the body and a bibliography entry**. A technical citation buried only in a BibTeX file is not attribution.
- Reuse credible secondary sources for background orientation as needed, while respecting original priority; a later survey is not automatically the originating result.
- Do not output unresolved citations as `\cite{Invented2020}` or fabricate placeholder bibliography entries. Place a clear `% TODO (citation audit): ...` comment in an unverified draft, plus an audit blocker.

## Consistency audit

For every `\cite{key}` used in the manuscript, check the key occurs once in the `.bib` and points to the intended genuine source. Check unused `.bib` entries, duplicate works under different keys, author spelling, DOI consistency, and contradictory preprint/published versions. Check quoted theorem numbers against source version. Report any unavoidable exception rather than silently claiming everything is verified.

## Minimal compilation/testing checklist

When tools allow: compile the LaTeX source, run BibTeX/Biber appropriate to the chosen toolchain, then recompile and inspect warnings for undefined control sequences, undefined citations and refs, duplicate labels, and missing bibliography files. If no compiler is available, perform text-level consistency checks and disclose the limitation. No tool use should be claimed unless performed.
