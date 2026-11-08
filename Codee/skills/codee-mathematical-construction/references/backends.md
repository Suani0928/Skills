# Computational backend selection, execution and exactness

## No assumed runtime
Available tooling differs by session. Before any execution: determine exactly which host tools, commands and software licenses are accessible. A skills-only plugin does not provision SageMath/Magma/Mathematica/etc., remote kernels, or local file permissions. If unavailable, produce concrete runnable source and honest `NOT_RUN`; never invent CAS API names or output.

## Backend preferences and hazards

| System | Typical strengths | Avoid overclaiming |
|---|---|---|
| SageMath | Number fields, finite fields, elliptic curves, function fields, symbolic/algebraic computation, interfacing other systems | No general automatic algorithm for arbitrary smooth projective models, Picard groups or cohomology |
| Macaulay2 | Graded modules, free resolutions, sheaves, Ext, Tor, local and sheaf cohomology in supported presentations | `HH^i` requires correctly defined projective scheme and coherent sheaf; cannot replace geometry with unrelated module |
| Magma | Group theory, invariant theory, elliptic curves and arithmetic, number fields, finite and function fields | Many higher-dimensional geometric computations need special hypotheses, algorithms and paid license |
| Mathematica | Exact symbolic transforms, elimination, polynomial algebra, local series and pattern checks | Symbolic simplification may assume generic parameters/branches; inspect assumptions, complex roots and exceptional loci |
| GAP | Finite groups, character tables, modular representations, HAP group cohomology | Does not natively solve arbitrary coherent sheaf cohomology; check installed GAP packages |
| Python | Test orchestration, precise code packaging, SymPy/Sage-style custom algorithms, provenance | Native Python float not a rigorous exact proof; numerical libraries need certification |
| Singular | Gröbner bases, ideals, primary decomposition, singularity-local algebra, normalizations where supported | Local computations do not prove global Picard equivalence, properness or full model construction without linking evidence |

Expandable backends by need: PARI/GP, FLINT, Oscar/Julia, CHEVIE, MATLAB, Macaulay2 packages, Lean/Rocq/Isabelle (proof checkers, not generic CAS), specialized libraries. Choose **mathematical capability** first; user-requested languages may be output targets even when not in the seven initial systems.

## Dispatch steps
1. Record `claim → representation → algorithm → required capabilities → candidate backend`.
2. Check current API/version and license using installed help or authoritative current documentation if accessible; avoid invented function names. If uncertain, label a call unverified.
3. Generate exact input, reproducible command, minimal runtime dependencies, assertions and expected mathematical *property* (rather than an unverified numeric answer).
4. Compare algebraic equality and invariants using independent checks, ideally different algorithmic formulation; if the same CAS verifies its own derivation, describe the dependence.
5. Separate source-language code from verified execution logs and generated outputs; do not embed fabricated logs.

## Exactness
Explicitly declare: `EXACT` (Q, number field, finite field, symbolic ring, rigorous exact quotient), `CERTIFIED_NUMERIC` (interval/error bound + theorem linking bound to claim), `HEURISTIC_NUMERIC`, or `FINITE_SAMPLE`. Record characteristic, embeddings, root choices, characteristic-dependent exceptions, term order, precision, seed and random search exhaustiveness.

For generic/universal statements, proving by finite testing requires an *explicit exhaustive bound or theorem*. For base change and reduction, record discriminant, denominators, bad primes and needed comparison theorem before lifting information.
