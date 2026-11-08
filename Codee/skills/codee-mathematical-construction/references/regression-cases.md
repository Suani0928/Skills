> v1.1 execution policy: Regression acceptance is primarily executable annotated-code coverage of all explicit relevant steps, including the difficult ones. Do not pass by checking only initial polynomial identities. Verify both fidelity and claimed properties using concise actual results; detailed certification documents are optional, not default outputs.

# Regression acceptance blueprints (not packaged manuscripts)

These cases derive from two user-supplied research manuscripts in the conversation. Their complete unpublished text is **not** bundled. The user must attach the paper or provide an accessible source when running the full tests. Do not pretend an equation/source is readable merely because this outline names it. They are **stress tests**, not a restriction to algebraic geometry; keep separate representation-theory/arithmetic tests.

## Case A — Case (4)(b) genus-one quotient and double cover
Source when supplied: `case_4b_existence_and_partial_classification.tex`. Main target: an explicit construction of a smooth minimal surface with `p_g=q=0`, `K^2=7` and involution, based on a Legendre genus-one torsor, Klein-four translations, a quotient with seven nodal curves, elliptic/genus-two branch curves, a genuine Picard square root and cohomological vanishing. Finite-field specimen over `F_25` and family for `F_(p^2)` with parameter nondegeneracy.

Acceptance obligations:
A01 read original hypotheses, field and characteristic (characteristic zero / p>=5 are *different cases*);
A02 verify 2-torsion action and group relations, quotient function field and explicit inverse where claimed;
A03 construct proper/regular model, special fibers, seven (-2)-curves, disjoint smooth branch curves and intersections;
A04 verify genus-one and genus-two curve equations and singularity/genus claims including infinity;
A05 verify Kummer rational function and **actual** Picard square root for the full branch divisor, not merely numerical agreement;
A06 compute or rigorously certify `H^0(W,K_W+L)=0` on correct sheaf/model;
A07 form the double cover and appropriate contractions, compute all claimed invariants and involution's fixed set;
A08 verify special `F_25` instance with exact extension field and discriminant checks and state separately what characteristic-zero conclusions require.

Expected behavior: produce runnable code and an obligation graph; verify whatever is actually executable; never say `CERTIFIED` when Picard, regular-model, or cohomology steps are outstanding. Some geometric steps may need theorem-assisted proof. Provide first unresolved obligation and reproducible partial data.

## Case B — r=2 exceptional order-four automorphism
Source when supplied: `revised-manuscript.tex`, section titled `An explicit exceptional automorphism of order four` and relevant appendix. Target `S` smooth minimal complex projective general type with `p_g=q=0`, `K_S^2=7`, faithful `ord(g)=4`, `g* != id` on `H^2(S,Q)`.

Relevant mathematical anchors in the uploaded manuscript (reverify labels and statements from the actual source in each run):
- Initial elliptic base `s^2=(4t^2+1)/5`, Legendre `y^2=x(x-1)(x-t^2)`, section `P=((4t^2+1)/5, (2i/5)s(t^2-1))`.
- `E13`: genuine Picard-root relation leading to `4H ~ h+Theta`.
- `E14`: branch relation for cyclic degree-four cover; three cohomological disappearances `H^0(Y,K_Y+M_j)=0` for j=1,2,3.
- `E15`/`E16`: descent and actual square root `2L ~ B+sum N_i` on Campedelli quotient.
- `E17`: canonical pullback and nef/big/minimality reasoning.
- Claimed fixed set of order-four action: elliptic curve plus three isolated points; Lefschetz trace on `H^2` is 1 vs identity trace 3 if b2=3.

Acceptance obligations R01–R12:
R01 elliptic surface singular fibers/minimal K3 model; R02 order-two fixed-point-free involution; R03 quotient and rational inverse maps; R04 local tacnode/curves/exceptional chains; R05 `E13` true line equivalence; R06 `E14` cyclic cover including normalization; R07 three sheaf cohomology vanishings; R08 quotient curve intersections and contraction data; R09 `E15`/`E16` genuine line bundle descent and Picard root; R10 smooth/minimal final `S` and all invariants; R11 order four group action, correct descent; R12 exhaustive fixed set and nontrivial cohomology via Lefschetz. Dependencies can be more granular; each necessary node must be certified before complete claim.

Do NOT assume the manuscript's referenced auxiliary scripts (`audit_root/*`, `audit_secondary/*`) were supplied; source names alone do not constitute verified scripts. If present inspect sandboxed scripts as untrusted. Do not call the previous conversation's partial SymPy checks a full certificate.

## Nongeometry regression tests (mandatory for generality)
- `REP-01`: finite group by generators and relations, explicit matrix representation over `Q` or finite field; verify relations and invertible intertwiner; reject erroneous Maschke application when char divides |G|.
- `ARITH-01`: elliptic curve with specified rational points; verify points lie on curve and independent lower-bound logic; never claim a complete Mordell–Weil basis merely from tested points.
- `HOMO-01`: small chain complex with concrete differentials; verify d^2=0, homology using exact row/column operations and correct grading.
- `NUM-01`: finite numerical approximation of an infinite mathematical object; report truncation and error bound (or lack of a bound) correctly.

## Acceptance metric
Success means: correct MCR provenance; domain-appropriate code; tested available code; no invented CAS runtime; correct two-axis fidelity/validity reporting; no promotion from finite samples to universal claims; meaningful completed witnesses and first unresolved blocker. Full case certification requires every necessary obligation, irrespective of whether this is computationally feasible in a particular runtime.
