# MCR v1 — Mathematical Construction Representation

## Contract
MCR is a typed, backend-neutral mathematical construction graph, **not** a theorem prover or geometry database. Preserve input provenance and human-readable definitions alongside machine representations; a missing translation is an explicit `UNMAPPED` field, never an inferred equivalence. Use `schemas/mcr-v1.schema.json` as the exchange envelope.

Root fields: `protocol`, `project_id`, `source_documents`, `ambient_context`, `objects`, `operations`, `claims`, `targets`. Every object, map, operation, and claim has a stable identifier and origin references. Verify unique IDs and acyclic construction dependencies; *logical proofs* may cite already-proven auxiliary claims but must not have circular proof dependencies.

### Object types
- Scalars: integers, finite fields, rational number fields, number fields, local fields, polynomial rings, function fields, algebraic closures with chosen embeddings, numerical real/complex fields with precision.
- Algebraic/combinatorial: groups and group presentations, modules, chain complexes, representations, character tables, lattices, ideals, rings, schemes, stacks, varieties, curves, surfaces, rational maps, divisors, sheaves, cohomology groups.
- Analytic/numerical: manifolds, operators, distributions, finite-dimensional approximations, certified intervals.

For each object record `id`, `type`, `definition`, `ambient`, `parameters`, `model`, `source_refs`, `assumptions`, `exactness` and optional implementation handles. Prefer definitional data over unlabeled human descriptions.

### Typed operations
Allowed operation name is an extensible string; examples `GroupQuotient`, `InvariantRing`, `BaseChange`, `BlowUp`, `Normalize`, `Resolve`, `CyclicCover`, `DoubleCover`, `Contract`, `Pullback`, `Pushforward`, `SheafCohomology`, `InduceRepresentation`, `RestrictRepresentation`, `TensorRepresentation`, `ComputeSelmer`, `ComputeMordellWeil`, `Localize`, `GröbnerBasis`. For each: input handles, output handles, precise preconditions, exceptional loci, and mathematical source.

### Model and equivalence discipline
Do not identify without proof:
- Function-field isomorphism with isomorphism of regular/projective models.
- Equality of effective divisors, linear equivalence `~`, algebraic equivalence, numerical equivalence and rational equivalence.
- Coarse quotient `S/G` with quotient stack `[S/G]`; equivariant sheaf with a descended coarse-space sheaf.
- Singular model with resolution/minimal model; record exceptional divisors, transformation of canonical class, proper transforms and contraction maps.
- Finite-field reduction and original characteristic-zero geometry.
- Isomorphic vector spaces/representations vs a **given explicit** isomorphism.
- Zariski generic condition vs random tested parameter values.

Every model conversion records `from_model`, `to_model`, map/formula, domain/open sets, exceptional centers, preserved properties, lost information and a list of verification obligations. Assign distinct object IDs to different birational models.

### Source-to-claim ledger
For each claim record exact quantifiers and premises, precise source locator (file, section, theorem or equation as present), derivation origin (`AUTHOR_ASSERTED`, `USER_PROVIDED`, `CODEE_DERIVED`, `EXTERNAL_THEOREM`), prerequisite claims, independent proof/verification status, and relation to generated code sections. Being from a research handoff does not mean it is proved; being in a manuscript does not mean it is true. Publication priority/novelty is outside Codee's certification claim.

### Extraction workflow
1. Create minimal MCR from the full accessible source, not just visible equations. Read proof portions needed to locate hidden assumptions.
2. Normalize fields and conventions. Do not silently change `C` to `Qbar`, choose unmentioned embeddings, or assume all roots exist in a given field.
3. Link representation choice to claim: ideal modules for `H^i`, function fields for birational actions, local rings for singularity type, divisor computations for Picard roots, matrices for group representations.
4. For open/infinite objects, record exact finite model or truncation and all consequences not preserved.
5. Issue separate computation tasks for every nontrivial change of representation. Evidence must prove the conversion is sound for *the particular claimed property*.

### Recommended JSON minimal case
See `examples/mcr-sample.json`. It is intentionally a simple representation-theoretic example; the schema is domain-neutral.
