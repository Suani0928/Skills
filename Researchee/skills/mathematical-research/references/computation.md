# Computation in mathematical research — on-demand guide

Use computational tools when they provide decisive tests, candidate constructions, exact identities, or rigorously verifiable evidence. Do not run lengthy searches merely to signal effort.

## Preferred practice

- Prefer exact symbolic or arithmetic computation when possible; distinguish floating-point evidence from mathematically exact identities.
- Record essential inputs: equations, coefficients, parameter choices, base ring/field and characteristic, conventions, precision or search bounds, software and code when relevant.
- State whether the computation explores examples, tests a necessary condition, gives an exhaustive search within a finite universe, or contributes to a proof.
- Recheck important calculations by an independent method when feasible; verify that computational assumptions match the original mathematical object.
- If computation is unavailable or was not run, present an algorithm or proposed experiment as **unexecuted**. Do not invent outputs.

## What computation does not automatically establish

A finite list of examples does not prove a universal statement. A failed bounded search does not prove nonexistence outside that bound. An example over a finite field does not by itself solve a complex or characteristic-zero existence problem. An approximate numerical observation does not by itself prove an exact algebraic identity.

A computational claim may be promoted to a rigorous proof only when the mathematical reduction, algorithmic correctness, and sufficient/exhaustive coverage are justified and can be independently checked.

## Reporting

Keep the main mathematical report focused on results and implications. Include only the minimum reproducibility data there; preserve essential detailed commands or outputs in an appendix or the Research Continuation Record if they are needed for further work.
