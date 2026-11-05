# PROMETHEUS // Quantum Execution Intelligence

Hardware-aware quantum compilation, pre-execution candidate selection, and multi-QPU dispatch across heterogeneous quantum processors.

**Portfolio Scope:** Prometheus operates both as a **hardware-aware quantum compiler** and as a **multi-compiler execution-selection layer** evaluating candidate physical implementations from **Prometheus**, **Qiskit SABRE O3**, and **Quantinuum TKET** across **IBM Quantum** (`ibm_fez`, `ibm_marrakesh`, `ibm_kingston` 156Q Heron r2), **IQM Resonance** (IQM Emerald 54Q, IQM Garnet 20Q), and **Amazon Braket** (Rigetti Cepheus-1-108Q, IQM Garnet 20Q, IQM Emerald 54Q).

---

## 1. Executive Summary & Representative Studio Benchmark

> [!NOTE]
> **Metric & UI Conventions:**
> - **Classical Distribution Overlap (F_B, ↑ higher is better) vs. Squared Hellinger Fidelity (F_H = F_B², ↑ higher is better):** F_B(P_ideal, P_meas) = Σ_x √(P_ideal(x) · P_meas(x)); F_H = F_B². Note that the Studio UI label `"State Fidelity [?]"` displays F_B.
> - **Total Variation Distance (TVD, ↓ lower is better):** 0.5 · Σ_x |P_ideal(x) - P_meas(x)|.
> - **Heavy-Output Probability (HOP, ↑ higher is better)** and **Linear Cross-Entropy (XEB, ↑ higher is better)**.

### Table 1A: Multi-Cloud Benchmark Campaign Summary

| Benchmark Campaign | Target Processors | Scope & Sample Size | Summary Outcome |
| :--- | :--- | :--- | :--- |
| **IQM Emerald Dense-Circuit Optimization & Matched Placement** | IQM Emerald (54Q) | 19 complete-block jobs (739 physical circuits, 756,736 shots across 7Q-17Q, 297.00 credits) | **+3.73%** workload-averaged F_B *(mean)* vs. SABRE K8 (p = 2.73 × 10⁻⁸, 39/48 wins) & **+7.57%** vs. Pure TKET K8 (p = 4.97 × 10⁻¹⁴, 46/48 wins); **+5.40%** (16/16 wins, p = 3.05 × 10⁻⁵) under matched physical placement; **+9.37%** (12/12 wins, p = 4.88 × 10⁻⁴) at 13Q-17Q |
| **IQM Resonance Spatial Multiplexing & Held-Out Scheduler** | IQM Emerald (54Q), IQM Garnet (20Q) | 40 scored jobs (740 physical PUBs, 1,196 workload evaluations, 378,880 shots) | **3.30x** active-QPU throughput (**3.00x** per credit) at 4-Way multiplexing (120/120 workloads ≥ 0.90); **99.0%** loss recovery (0.9458 vs. 0.9078 F_B) on Stage 4B boundary-stress held-out suite |
| **IBM Heron Extended 1,023-Circuit Validation** | `ibm_fez`, `ibm_marrakesh`, `ibm_kingston` (156Q) | 17 batch jobs (1,023 physical circuits, 1,047,552 shots across 4 pillars) | **+3.27%** mean F_B (**+5.42%** F_H, **-12.05%** 2Q gates) vs. SABRE O3 across 432 Pillar 1A circuits, expanding to **+6.67%** F_H with pre-execution QPU dispatch; **0.2589** vs. 0.2281 SABRE O3 at 101Q Clifford mirrors |
| **AWS Braket Multi-Window Rigetti Replication** | Rigetti Cepheus-1-108Q (108Q) | 10 `ProgramSet` tasks (450 physical circuits, 460,800 shots across 3 calibration windows) | **+3.91%** 3-window workload-averaged F_B *(mean)* vs. SABRE O3 (p_Holm = 0.0112) and **+9.03%** vs. TKET (p_Holm = 0.000641), with **-13.35%** fewer 2Q gates and **-23.56%** lower depth |
| **IBM Heron 8-Way Spatial Multiplexing & Meta-Selection** | `ibm_fez`, `ibm_marrakesh`, `ibm_kingston` (156Q) | 19 jobs (586 physical PUBs, 1,140 workload evaluations, 655,360 shots) | **2.85x** qualifying workloads per billed second (**-57.1%** billed time) on `ibm_marrakesh` (11/16 vs. 9/16 ≥ 0.90); TKET buffered 8-Way packing improves F_B by **+0.0031** over isolated TKET (p = 0.0117) |
| **Pre-Committed 144-Execution Suite & Heron 156Q Matrix** | `ibm_marrakesh`, `ibm_fez`, `ibm_kingston` (156Q) | 10 packed `SamplerV2` jobs (441 physical circuits, 755,712 shots: 297 in 99 tournaments + 144 pre-committed) | **16/18 (88.9%)** primary metric wins vs. SABRE O3 (15/18 vs. TKET) on pre-committed suite; **65/99 (65.7%)** wins vs. SABRE O3 (89/99 vs. TKET) across 3Q-13Q odd/even & 15-family matrix |
| **Multi-Cloud 3-Way Corpus (107 Heron + 12 Braket)** | 3 IBM Heron (156Q), Rigetti (108Q), 2 IQM (20Q/54Q) | 119 completed jobs/tasks (357 physical circuits, 5,084,160 shots) | **80/107 (74.8%)** wins vs. SABRE O3 and **100/107 (93.5%)** wins vs. TKET on Heron (4Q-23Q); **9/12** fidelity wins and **12/12 (100.0%)** depth & 2Q gate reductions on Braket |

### Table 1B: Representative 3-Way Studio Execution - 9-Qubit Dense All-to-All (K_9) on `ibm_marrakesh` (Job ID: `dadl5jd1ierc738l1420`, 4,096 Shots/Compiler)

| Metric & Direction | Qiskit SABRE O3 | Quantinuum TKET | Prometheus | Prometheus vs. Best Baseline |
| :--- | ---: | ---: | ---: | ---: |
| **Compiled Circuit Depth (↓)** | 145 | 165 | **109** | **-24.83%** |
| **Native Two-Qubit CZ Gates (↓)** | 90 | 123 | **74** | **-17.78%** |
| **Distribution Fidelity F_B (↑)** *(Studio UI: "State Fidelity")* | 0.5738 | 0.5248 | **0.7466** | **+30.12%** |
| **Heavy-Output Probability HOP (↑)** | 0.6975 | 0.7339 | **0.8425** | **+14.80%** |
| **Total Variation Distance TVD (↓)** | 0.4572 | 0.5241 | **0.3015** | **-34.04%** |
| **Linear Cross-Entropy XEB (↑)** | 38.3213 | 31.1110 | **50.1079** | **+30.76%** |

[![9Q Dense All-to-All 3-Way Execution Result](screenshots/07-qv-execution-result.png)](screenshots/07-qv-execution-result.png)

*Figure 1: Prometheus Execution Studio 3-Way Comparative Benchmark (SABRE O3 vs. TKET vs. Prometheus) on 9-Qubit Dense All-to-All (K_9), executed on `ibm_marrakesh` (Job ID: `dadl5jd1ierc738l1420`, 4,096 shots/compiler = 12,288 total shots).*

---

## 2. Core Execution Workflow & Repository Guide

```text
Logical Quantum Circuit (OpenQASM 2.0 / 3.0)
        |
        +---> Prometheus Hardware-Aware Compiler
        +---> Qiskit SABRE O3 Baseline
        +---> Quantinuum TKET Baseline
                    |
                    v
   Physical Candidate Verification & Calibration Scoring
                    |
                    v
   Pre-Execution Candidate & Target-QPU Selection
                    |
                    v
   Packed Hardware Execution (IBM SamplerV2 / AWS Braket ProgramSet / IQM Resonance)
                    |
                    v
   Canonical Logical Measurement Recovery & Offline Scoring
```

- **[`SCREENSHOT_GALLERY.md`](SCREENSHOT_GALLERY.md)** - Complete 18-screenshot visual walkthrough of Prometheus Studio (01-06: Configuration; 07-10: 9Q Dense All-to-All 3-Way Benchmark `dadl5jd1ierc738l1420`; 11: 8Q Quantum Volume `dabeu63vpcac73ddn40g`; 12-14: 9Q Repeated-Run Drift Controls; 15-18: 12Q-16Q Dense All-to-All Comparisons).
- **[`results/RESULTS.md`](results/RESULTS.md)** & **[`demonstrations/DEMONSTRATIONS.md`](demonstrations/DEMONSTRATIONS.md)** - Detailed metric tables and Job ID index for the Studio screenshots.
- **[`ARCHITECTURE.md`](ARCHITECTURE.md)** - Multi-compiler candidate evaluation and multi-QPU dispatch architecture.
- **[`PROJECT_DIRECTION.md`](PROJECT_DIRECTION.md)** - Cross-paradigm roadmap across superconducting, trapped-ion, and neutral-atom processors.
- **[`PUBLIC_DISCLOSURE.md`](PUBLIC_DISCLOSURE.md)** - Public verification artifacts vs. protected compiler internals.

---

## 3. Prometheus Dynamics Public Repository Portfolio (9 repositories | 248 benchmark jobs | 5,110 physical circuits/PUBs | 13,264,640 physical shots)

**Portfolio Totals:** 9 Verified Repositories | 248 Completed Benchmark Jobs/Tasks (167 IBM Heron Jobs, 22 AWS Braket Tasks, 59 IQM Resonance Jobs) | 5,110 Physical Circuits/PUBs | 13,264,640 Physical Measurement Shots

Counts refer to completed public benchmark executions, excluding simulations, classical GPU runs, unrecovered queue dispatches, and two setup smoke tests. Shared datasets are counted once: the shared 4-job (144-circuit, 147,456-shot) pre-committed validation suite is counted in `IBM-Heron-156Q-Benchmarks`, and all 33 archived job ZIP bundles (99 circuits, 1,622,016 shots) in `qpu-selection-execution-quality` already occur in the 107-job historical IBM Heron corpus (`Hybrid-Quantum-HPC-Benchmarks`). The telemetry archive (`prometheus-quantum-telemetry`) contributes 774 PUBs and 4,125,440 physical shots across 14 jobs, counted directly from archived measurement arrays. Physical multiplexed shots are not multiplied by the number of component workloads.

| Repository | Scope & Empirical Dataset | Primary Verification Artifacts |
| :--- | :--- | :--- |
| **[`IQM-Resonance-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing)** | **IQM Emerald (54Q) Dense-Circuit Optimization & Spatial Multiplexing:** 59 scored hardware jobs (1,479 physical circuits/PUBs, 1,935 workload evaluations, 1,135,616 physical shots): 19-job Dense-Circuit Optimization, Odd/Even Parity, & Matched-Placement Campaign (739 circuits, 756,736 shots, **+3.73%** vs. SABRE K8, **+7.57%** vs. Pure TKET K8, **16/16** matched-placement wins) + 40-job Spatial Multiplexing & Prospective Scheduler Campaign (740 PUBs, 1,196 evaluations, **3.30x** 4-Way throughput). | [`data/dense_campaign_stages2_3_4_results.json`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/data/dense_campaign_stages2_3_4_results.json), [`data/stage2_emerald_replication_results.json`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/data/stage2_emerald_replication_results.json), [`scripts/verify_iqm_resonance_ledger.py`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/scripts/verify_iqm_resonance_ledger.py) |
| **[`Quantum-Execution-Manager-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing)** | **IBM Heron 8-Way Spatial Multiplexing & Multi-Compiler Meta-Selection:** 19 completed hardware jobs (586 physical PUBs, 1,140 workload evaluations, 655,360 physical shots) across `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston` (**2.85x** qualifying workloads per billed second, **-57.1%** billed time, and SABRE/TKET/Prometheus interoperability). | [`data/campaign3_compiler_interoperability_results.json`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing/blob/main/data/campaign3_compiler_interoperability_results.json), [`scripts/verify_spatial_multiplexing_campaigns.py`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing/blob/main/scripts/verify_spatial_multiplexing_campaigns.py) |
| **[`IBM-Heron-Extended-Validation-1023-Circuits`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits)** | **4-Pillar Extended IBM Heron r2 Validation (1,023 Circuits):** 17 batch jobs (1,023 physical circuits, 1,047,552 physical shots) across `ibm_marrakesh`, `ibm_fez`, and `ibm_kingston` (**+3.27%** mean F_B vs. SABRE O3 in Pillar 1A, **+6.67%** F_H with QPU dispatch, and 8Q-101Q Clifford mirror scaling). | [`ALL_1023_CIRCUITS_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits/blob/main/ALL_1023_CIRCUITS_RESULTS.csv), [`scripts/verify_campaign.py`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits/blob/main/scripts/verify_campaign.py) |
| **[`AWS-Braket-Multi-Window-Validation`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation)** | **Rigetti Cepheus-1-108Q 3-Window Replication & Cross-Provider Comparison:** 10 AWS Braket `ProgramSet` tasks (450 physical circuits, 460,800 physical shots) across 3 calibration windows (**+3.91%** vs. SABRE O3, p_Holm = 0.0112; **+9.03%** vs. TKET, p_Holm = 0.000641). | [`data/ALL_450_BRAKET_CIRCUITS_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation/blob/main/data/ALL_450_BRAKET_CIRCUITS_RESULTS.csv), [`scripts/verify_braket_campaign.py`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation/blob/main/scripts/verify_braket_campaign.py) |
| **[`IBM-Heron-156Q-Benchmarks`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks)** | **156Q Heron r2 Scaling & Pre-Committed Suite:** 10 packed `SamplerV2` batch jobs (441 physical circuits, 755,712 shots) across `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston` covering 3Q-13Q odd/even parity scaling, a 15-algorithm matrix at 9Q (297 circuits), and the 144-execution pre-committed validation suite (4 jobs). | [`data/heron_156q_99tournaments_297circuits.csv`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/blob/main/data/heron_156q_99tournaments_297circuits.csv), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/tree/main/validation_suite_144_executions), `scripts/verify_ledger.py` |
| **[`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks)** | **Multi-Cloud QPU & Hybrid GPU Corpus:** 119 unique 3-way QPU jobs/tasks (357 physical circuits, 5,084,160 shots: 107 IBM Heron jobs / 321 circuits / 4,964,352 shots + 12 AWS Braket `ProgramSet` tasks / 36 circuits / 119,808 shots), plus the shared 144-execution pre-committed suite and 150 NVIDIA H100 (`VeloxQH100_1`) QUBO runs (4 to 1,029 variables). | [`aws_braket_qpu_12_jobs_ledger.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/aws_braket_qpu_12_jobs_ledger.json), [`ibm_heron_156q_verified_benchmarks.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/ibm_heron_156q_verified_benchmarks.json), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/tree/main/validation_suite_144_executions), `verify_corpus_and_schedules.py` |
| **[`qpu-selection-execution-quality`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality)** | **Cryptographic Provenance & Cross-QPU Arbitration:** 33 archived IBM Quantum job ZIP bundles (99 physical circuits, 1,622,016 shots across 16Q-23Q in `Fez/`, `Kingston/`, `Marrakesh/`, and 20Q-22Q broadcast runs in `Fez_Marrakesh_Kingston/`, already counted in the 107-job historical IBM corpus) plus the shared 4-job 144-circuit pre-committed suite. | [`EVIDENCE_INDEX.md`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/EVIDENCE_INDEX.md), [`REPOSITORY_SHA256SUMS.txt`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/REPOSITORY_SHA256SUMS.txt), `Fez_Marrakesh_Kingston/3_verify_and_view.py` |
| **[`prometheus-quantum-telemetry`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry)** | **Mechanistic Operating Envelope (01-05):** 14 IBM Heron jobs (774 physical PUBs, 4,125,440 physical shots across all 14 archived `job-*-result.json` measurement arrays; 417 normalized circuit rows in `MASTER_RESULTS.csv` for Experiments 01-03) covering distributional concentration (100k shots/circuit), 40 randomized matched pairs, 3Q-10Q scaling boundaries, 13Q ground-state avoidance, and a 540-PUB (1,105,920-shot) 3-QPU mechanistic sweep. | [`IBM_JOB_EVIDENCE_INDEX.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/IBM_JOB_EVIDENCE_INDEX.csv), [`MASTER_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/MASTER_RESULTS.csv), `verify_sha256_evidence.py` |
| **[`prometheus-execution-intelligence`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence)** | **System Architecture & Consolidated Multi-Cloud Index:** Multi-compiler candidate evaluation (SABRE O3, TKET, Prometheus), multi-QPU dispatch workflow, and 18-screenshot Studio visual gallery indexing the 248 completed benchmark jobs/tasks across 6 QPUs. | [`ARCHITECTURE.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/ARCHITECTURE.md), [`SCREENSHOT_GALLERY.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/SCREENSHOT_GALLERY.md) |

> **Deduplicated Portfolio Accounting Note:** Summing the deduplicated per-repository completed hardware counts across the 8 empirical data repositories (`59 + 19 + 17 + 10 + 10 + 119 + 0 + 14`) yields **248 completed benchmark jobs/tasks** (167 IBM Heron jobs, 22 AWS Braket tasks, and 59 IQM Resonance jobs), **5,110 physical compiled circuits/PUBs** (`1,479 + 586 + 1,023 + 450 + 441 + 357 + 0 + 774`), and **13,264,640 physical measurement shots** (`1,135,616 + 655,360 + 1,047,552 + 460,800 + 755,712 + 5,084,160 + 0 + 4,125,440`). Shared datasets are counted once (`IBM-Heron-156Q-Benchmarks` includes the 4-job 144-circuit pre-committed suite, and `Hybrid-Quantum-HPC-Benchmarks` includes all 33 archived job ZIPs from `qpu-selection-execution-quality`).

---

**Website:** https://prometheusdynamics.ca  
**Organization:** https://github.com/PrometheusDynamicsCanada
