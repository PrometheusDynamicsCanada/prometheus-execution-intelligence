# PROMETHEUS // Quantum Execution Intelligence

**Hardware-aware quantum compilation and execution intelligence for generating, evaluating, selecting, and dispatching physical quantum executions across heterogeneous QPUs.**

Prometheus is both a **quantum compiler** and a **hardware-aware execution-intelligence system**.

The Prometheus compiler performs circuit compilation, physical mapping, and routing while incorporating information about the target hardware into the optimization process. Prometheus can also evaluate alternative compiler outputs—including **SABRE O3** and **TKET**—as competing execution candidates.

The result is an execution architecture in which compilation and execution selection are treated as related, but distinct, problems:

> **Generate a physical circuit. Understand the hardware. Select the execution. Dispatch it to the QPU. Measure what happened.**

---

## What is Prometheus?

Prometheus is a hardware-aware quantum compiler and execution-intelligence system for heterogeneous quantum computing environments.

Rather than treating the output of a single compiler as the final execution, Prometheus can generate and evaluate multiple physical realizations of the same workload and select an execution based on the target hardware and available execution data.

At a high level:

```text
                          Quantum Workload
                                │
                                ▼
                    ┌─────────────────────────┐
                    │ Candidate Generation    │
                    │                         │
                    │ Prometheus Compiler     │
                    │ SABRE O3 / Qiskit       │
                    │ TKET                    │
                    │ Other candidates        │
                    └────────────┬────────────┘
                                 │
                     Physical execution candidates
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
             Hardware State           QPU Capabilities
                    │                         │
                    └────────────┬────────────┘
                                 ▼
                    Hardware-Aware Evaluation
                                 │
                                 ▼
                    Execution Intelligence
                                 │
                                 ▼
                     Compiler / Circuit / QPU
                            Selection
                                 │
                                 ▼
                           Job Dispatch
                                 │
                                 ▼
                        Observed Execution
                                 │
                                 ▼
                    Execution / Drift Telemetry
