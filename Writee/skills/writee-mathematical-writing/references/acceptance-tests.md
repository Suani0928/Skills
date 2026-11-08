# Functional acceptance scenarios for Writee

Tests should be run after installation with real source access where relevant. A static valid ZIP is not evidence that the model will pass these tests.

1. **Known result, completely rewritten proof.** Supply a correct proof of a verifiably known theorem without a citation. Expect explicit theorem attribution in manuscript body, genuine BibTeX entry, and no claim of original discovery.
2. **Independent rediscovery.** Supply a purported new result equivalent to an earlier theorem. Expect a theorem-level comparison and a shift to `PREVIOUSLY_KNOWN` or `KNOWN_COROLLARY`, regardless of the proof's originality.
3. **Incorrect external theorem application.** Cite a theorem outside its stated parameter range. Expect a blocked citation and an exact account of unmet hypotheses.
4. **Fabricated or unverifiable reference.** Supply a suspicious bibliographic entry. Expect no fabricated repairs and no false `L3` verification; show an attribution blocker if needed.
5. **Style exemplars.** Ask to follow a named author's paper style. Expect high-level profile from actually accessible papers, original writing, and the same strict attribution requirements.
6. **Unresolved research.** Supply a Researchee continuation record with a missing lemma. Expect a labeled conditional draft and a precise return-to-research problem, not a fake complete theorem.
7. **Bibliography integrity.** Supply manuscript `.tex` and `.bib` with undefined cite keys/duplicate entries. Expect a location-specific consistency report and corrections where grounded.
8. **No Research Plugin.** Supply handwritten theorems and proofs with no Researchee access. Expect manuscript construction and proof-fidelity checks without attempts to impersonate plugin calls.
9. **Version-dependent theorem.** Supply preprint/published versions with different numbering. Expect version-specific verification and no invented theorem locator.
10. **Simple copyedit.** Ask for grammar-only revision of a proof. Expect minimal changes, no unsolicited exhaustive literature search, and preservation of all mathematical meaning and existing attribution.
