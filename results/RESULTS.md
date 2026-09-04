# Demonstration Results

## Scope of the current results

The current result set comes from an **early-stage prototype** operating with SABRE O3 and a limited set of IBM Quantum processors available through the IBM Quantum Free Tier.

These results are intended to demonstrate system operation and motivate further validation, not to establish universal performance claims.

The broader development direction is to repeat this evaluation across additional compiler strategies, processors, vendors, and quantum hardware technologies.

---

## Dense All-to-All — 9 qubits — IBM Marrakesh

The supplied Studio screenshot reports:

| Metric | Baseline | Prometheus | Displayed delta |
|---|---:|---:|---:|
| Execution cost reduction | — | — | **43.02%** |
| State Fidelity | 0.6815 | 0.7004 | **+2.77%** |
| Heavy Output Probability | 0.8289 | 0.8440 | **+1.83%** |
| Total Variation Distance | 0.3528 | 0.3308 | **-6.23%** |
| Cross-Entropy (XEB) | 11.4691 | 13.0769 | **+14.02%** |

These values are screenshot-derived and are included as representative demonstration evidence.

See the [Dense execution drift test 1](../screenshots/12-dense-execution-drift-test1.png), [drift test 2](../screenshots/13-dense-execution-drift-test2.png), and [drift test 3](../screenshots/14-dense-execution-drift-test3.png) screenshots for the repeated-run observations.

---

## Quantum Volume

The Quantum Volume demonstration consists of:

- [QV execution result](../screenshots/07-qv-execution-result.png)
- [QV hardware allocation](../screenshots/08-qv-hardware-allocation.png)
- [QV circuit structural characteristics](../screenshots/09-qv-circuit-structural-characteristics.png)
- [QV output state distribution](../screenshots/10-qv-output-state-distribution.png)
- [QV logical / compiled QASM](../screenshots/11-qv-logical-compiled-qasm.png)

These screenshots provide a completed comparative hardware execution and the associated result panels.

---

## Drift / repeated-circuit controls

The repeated executions are used to observe short-timescale run-to-run variation. They are treated as **controls for hardware variability**, rather than as isolated examples of routing failure.

This distinction matters because measured quantum-hardware quality can vary even when the workload and execution configuration are comparable.

---

## Interpretation

These demonstrations establish system operation and representative observed behavior. They should not be interpreted as a universal guarantee of improved fidelity for every workload, processor, compiler, or calibration state.

A favorable result is evidence of an observed outcome under a particular hardware and execution condition. A neutral or unfavorable observation is also useful because it defines the limits of the current prototype and motivates further investigation.

---

## Validation direction

The next stage of validation is to expand the candidate pool and hardware pool rather than optimize the narrative around one result. In particular, future work should test:

- multiple compiler outputs for the same workload;
- additional IBM Quantum processors;
- additional QPU providers;
- non-superconducting processor technologies;
- repeated A/B executions and hardware-variability controls;
- workloads with different topology and depth characteristics.
