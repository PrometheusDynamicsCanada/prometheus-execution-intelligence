# Architecture Overview

Prometheus separates **candidate compilation**, **hardware-aware candidate selection**, and **multi-QPU target dispatch** into distinct, verifiable stages.

```text
+----------------------------------------------+
|        Logical Workload (OpenQASM)           |
+----------------------------------------------+
                       |
                       v
+----------------------------------------------+
|            Candidate Generation              |
|  - Prometheus Hardware-Aware Compiler        |
|  - Qiskit SABRE O3                           |
|  - Quantinuum TKET                           |
+----------------------------------------------+
                       |
                       v
+----------------------------------------------+
|     Semantic & Measurement Verification      |
|  - Unitary / Reference Equivalence Check     |
|  - Canonical Logical Bit-Order Mapping       |
+----------------------------------------------+
                       |
                       v
+----------------------------------------------+
|   Pre-Execution Selection & QPU Arbitration  |
|  - Live Device Calibration Telemetry         |
|  - Pre-Committed Candidate & Backend Choice  |
+----------------------------------------------+
                       |
                       v
+----------------------------------------------+
|          Multi-Cloud QPU Execution           |
|  - IBM Quantum (ibm_fez, marrakesh, kingston)|
|  - Amazon Braket (Rigetti Cepheus, IQM)      |
+----------------------------------------------+
```

## Core Responsibilities

1. **Candidate Generation:** Produces multiple valid physical realizations of the same logical circuit in the target processor's native gate set (`CZ + SX/RZ/X` on IBM Heron, `CZ + PRX/RX/RZ` on Rigetti Cepheus and IQM Garnet/Emerald, and continuous-angle two-qubit bases on trapped-ion targets).
2. **Pre-Execution Selection:** Evaluates candidate circuits against active device calibration telemetry and commits a candidate choice prior to QPU execution. Internal scoring formulations, weights, and selection rules remain proprietary to Prometheus Dynamics.
3. **Multi-QPU Dispatch:** Evaluates candidate implementations across multiple available processors (`ibm_fez`, `ibm_marrakesh`, `ibm_kingston`, or across Amazon Braket QPUs) to route each workload to the physical device best suited to its interaction graph.
