# Domain-specific mathematical playbooks

The core is mathematical and domain-neutral. Use only the playbook matching the user's object; do not require geometry data for a representation problem, nor force a group-representation problem into a scheme. Expand beyond this list when justified by the paper.

## Algebraic geometry, elliptic surfaces, coherent cohomology
Types: base fields, curves/surfaces, projective or affine models, quotient schemes and stacks, rational/regular morphisms, equivariant sheaves, line bundles, Cartier/Weil divisors, NS/Picard group, branch data, resolution graphs, intersection matrices, cohomology. Critical checks:
- Finite group quotient with field characteristic and tame/wild action; stabilizers, invariant subrings, coarse vs stack quotient and descent of sheaves.
- Smooth/projective model vs function-field model; analyze base points, denominators, infinity, singular fibers and exceptional divisors when changing models.
- For cyclic n-fold cover, verify a genuine root line bundle and branch weights in `Pic` (not just NS), normality, normalization at crossings and covers over all charts. Check divisors in correct model.
- For blowups/resolutions/contractions, compute local equations, multiplicities, canonical discrepancies, exceptional intersections, and admissibility; geometric cohomology must be computed on the right sheaf/model.
- Elliptic curves: discriminant, Weierstrass minimal model, torsion, group law, isogenies, local data, rational points. Elliptic surfaces: fibration, zero section, singular fibers, sections/Mordell–Weil over function fields, Néron–Severi lattice, Shioda–Tate assumptions and fibers.
- `H^i(X,F)` over a finite tame quotient can reduce to invariants under appropriate derived push-pull and exactness assumptions; *do not* write a universal naive invariant formula outside its hypotheses, particularly for wild characteristic, unresolved sheaf descent, or singular/resolved different spaces.

## Representation theory
Types: finite/infinite groups, group algebra, generators and relations, fields, modules, matrices, characters, bilinear forms, categories/functors, quivers, Hecke algebras, Ext groups. Verify relations for generator matrices; representation homomorphism; invariant subspaces, module decomposition, irreducibility and intertwiners; explicit change-of-basis for claimed decomposition. Distinguish ordinary and modular characteristic; semisimplicity and character criteria depend on hypotheses. For a matrix representation, an explicit isomorphism must be invertible and commute with the generating matrices. GAP/Magma/Sage/CHEVIE as fits. Algorithms for large/infinite groups need restrictions.

## Arithmetic geometry and number theory
Types: global/local fields, rings of integers, schemes, elliptic/abelian varieties, Galois groups/representations, Selmer groups, heights, zeta/L functions, mod-p data. For Mordell–Weil claims distinguish independent points, rank lower/upper bound, saturation and full generators. For rational points separate locally soluble from globally soluble; for descent record Selmer local maps, primes and conditions. For Frobenius, track ramification, good reduction, embedding and normalization. Point counts can support trace or Euler factors for applicable good primes, but don't force global claims without applicable theorems. Numerical L-values require rigorous error bounds if used as proof.

## Commutative/homological algebra
Types: graded/filtered modules, chain complexes, resolutions, chain maps, spectral sequences, Gröbner bases, Ext/Tor, Hilbert functions, local cohomology. Verify differentials compose to zero, exactness at each degree, correct grading/sign convention, free resolution minimality when claimed, derived functor hypotheses, proper truncation bounds.

## Combinatorics, analysis, signal processing and other
For recurrences and combinatorial algorithms establish induction/invariants, termination and finite bounds. For infinite-dimensional or analytic structures select a faithful finite approximation or certified discretization with error theorem; do not equate truncation with original object. For signal processing check filter normalization, boundary conditions, unit conventions, stability, exact vs numerical transform, floating-point tolerances and conditioning.
