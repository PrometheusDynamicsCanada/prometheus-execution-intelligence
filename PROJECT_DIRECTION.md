# Project Direction

## What I want and what I need

A recurring question in discussions around Prometheus has been: **What do I want?**

There are two different answers.

## What I want

I want to continue doing the work itself:

- analyzing data;
- identifying systems that can be improved;
- designing mathematical and computational approaches to optimize those systems;
- applying that approach across scientific domains, not only quantum computing;
- turning analysis into practical systems;
- collaborating with researchers who are genuinely passionate about understanding difficult problems and building better systems.

Prometheus is one example of this approach. Quantum computing is the current experimental domain because it provides a particularly rich combination of physical hardware constraints, computation, uncertainty, and optimization.

The larger ambition is not to be defined by a single compiler, QPU, company, or scientific field. It is to keep doing rigorous analytical and systems-design work wherever there is a meaningful opportunity to improve an existing system.

## What I need

To do that work at a meaningful scale, I need the **funding and resources** to support sustained research and development.

That means access to:

- scientific and experimental infrastructure;
- quantum processors and other specialized hardware;
- computing resources;
- high-quality data;
- engineering support where useful;
- domain experts and research collaborators;
- an environment that allows long-term experimentation rather than one-off demonstrations.

The desired outcome is therefore broader than selling a single prototype. Commercialization can be one mechanism for sustaining the work, but the underlying objective is to create the resources and collaborations needed to continue analyzing data, designing systems, and testing improvements across increasingly difficult scientific problems.

## Prometheus as the current vehicle

The present Prometheus prototype is a concrete example of that philosophy.

Today it operates in a deliberately constrained environment:

```text
SABRE O3
   │
   ▼
IBM Quantum Free-Tier Processors
   │
   ▼
Prometheus hardware-aware execution selection
   │
   ▼
Real hardware execution
```

The development direction is broader:

```text
                    Quantum Workload
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       SABRE            TKET          Other compilers
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                 Execution candidates
                           │
                           ▼
               Hardware characterization
                           │
                           ▼
                PROMETHEUS ARBITRATION
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          IBM QPU     Quantinuum       IonQ
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                       Dispatch
```

The same abstraction is intended to extend beyond superconducting processors to other quantum hardware technologies as suitable interfaces and characterization data become available.

## Why the distinction matters

The current benchmark should be read as **evidence from an early prototype**, not as a claim that the complete multi-vendor architecture already exists.

The important result at this stage is that the basic execution-selection concept can be exercised on real hardware. That provides a foundation for expanding the candidate pool, the hardware pool, and eventually the dispatch layer itself.
