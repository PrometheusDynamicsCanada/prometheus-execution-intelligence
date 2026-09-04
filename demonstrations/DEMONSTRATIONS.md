# Demonstration Narrative

This document provides the intended walkthrough for the supplied screenshots. The screenshot filenames are descriptive and are used directly throughout this document.

---

## Demonstration 1 — Configure the prototype

Use screenshots **01–06**.

### 01 — Studio overview
[Open screenshot](../screenshots/01-studio-overview.png)

Show the main Prometheus Studio environment and the available operational controls.

### 02 — Target processor
[Open screenshot](../screenshots/02-target-processor.png)

Show how the target processor can be configured.

### 03 — Workload family
[Open screenshot](../screenshots/03-workload-family.png)

Show the workload-family selection.

### 04 — Search budget
[Open screenshot](../screenshots/04-search-budget.png)

Show the configurable candidate-search budget.

### 05 — Shot count
[Open screenshot](../screenshots/05-shot-count.png)

Show the execution shot-count configuration.

### 06 — Logical QASM
[Open screenshot](../screenshots/06-logical-qasm.png)

Show the logical workload presented to the execution system.

**Message:** Prometheus provides a single operational interface for preparing and dispatching hardware-aware quantum executions.

---

## Demonstration 2 — Evaluate and select

The current prototype uses **SABRE O3** as its candidate-generation baseline.

Prometheus evaluates multiple valid execution candidates against current hardware characterization and selects or retains an execution candidate.

The proprietary selection mechanism is intentionally outside the public repository.

**Message:** The prototype adds a hardware-aware evaluation and selection layer above existing compilation infrastructure.

---

## Demonstration 3 — Cross-QPU arbitration

The current prototype can assess supported IBM Quantum processors as potential execution targets.

**Message:** Processor selection can be workload-specific rather than based only on a static global ranking.

The longer-term direction is to extend the same abstraction to additional processors, vendors, and processor technologies.

---

## Demonstration 4 — Quantum Volume

Use screenshots **07–11**.

### 07 — QV execution result
[Open screenshot](../screenshots/07-qv-execution-result.png)

Completed comparative Quantum Volume execution and result summary.

### 08 — QV hardware allocation
[Open screenshot](../screenshots/08-qv-hardware-allocation.png)

Hardware allocation associated with the execution.

### 09 — QV circuit structural characteristics
[Open screenshot](../screenshots/09-qv-circuit-structural-characteristics.png)

Structural information exposed for the QV circuit.

### 10 — QV output state distribution
[Open screenshot](../screenshots/10-qv-output-state-distribution.png)

Observed output-state distribution.

### 11 — QV logical / compiled QASM
[Open screenshot](../screenshots/11-qv-logical-compiled-qasm.png)

Logical and compiled QASM views exposed by the interface.

**Message:** The system supports comparative hardware execution and exposes measured quality indicators, allocation information, circuit characteristics, compiled-circuit information, and output distributions.

---

## Demonstration 5 — Dense workload

Use screenshots **12–18**.

The Dense screenshots contain both repeated-run observations and topology/gain comparisons.

### Run-variation controls

- [12 — Dense execution drift test 1](../screenshots/12-dense-execution-drift-test1.png)
- [13 — Dense execution drift test 2](../screenshots/13-dense-execution-drift-test2.png)
- [14 — Dense execution drift test 3](../screenshots/14-dense-execution-drift-test3.png)

These repeated executions are included to observe short-timescale hardware/run variation.

### Observed gains / topology comparisons

- [15 — Observed gains topology comparison 1](../screenshots/15-observed-gains-topology-comparison1.png)
- [16 — Observed gains topology comparison 2](../screenshots/16-observed-gains-topology-comparison2.png)
- [17 — Observed gains topology comparison 3](../screenshots/17-observed-gains-topology-comparison3.png)
- [18 — Observed gains topology comparison 3 — depth comparison](../screenshots/18-observed-gains-topology-comparison3-depth-comparison.png)

The supplied demonstration set includes a representative 9-qubit Dense All-to-All execution on IBM Marrakesh with a displayed 43.02% execution-cost reduction and improvements across the displayed fidelity, HOP, TVD, and XEB metrics.

**Message:** The prototype can expose both favorable execution comparisons and the run-to-run variability that must be considered when interpreting real-hardware results.

---

## Demonstration 6 — Drift observation

The repeated Dense executions are treated as **hardware/run-variation controls**.

**Message:** Identical or comparable executions can vary across hardware runs. This variability is part of the operating environment and should be measured rather than hidden.

The controls therefore provide context for interpreting observed execution differences.

---

## Demonstration 7 — Where the prototype is going

The current system is intentionally limited to SABRE O3 and selected IBM Quantum processors.

The development direction is:

```text
SABRE / TKET / other compilers
             │
             ▼
   execution candidate pool
             │
             ▼
 hardware-aware arbitration
             │
             ▼
 compiler + circuit + QPU selection
             │
             ▼
        job dispatch
```

The hardware side is intended to expand from the current IBM-only environment toward additional IBM processors, Quantinuum, IonQ, and other quantum processor technologies.

The present repository demonstrates the first stage of that architecture. Additional compiler and provider integrations are future development.

---

## Demonstration principle

Always connect:

**workload → candidate generation → hardware-aware evaluation → selection → dispatch → observed result.**

The proprietary decision mechanism remains behind that interface.
