# Representative Studio Execution Results

This directory summarizes the hardware benchmark screenshots in [`../screenshots/`](../screenshots/). For complete machine-readable ledgers across all hardware campaigns, see [`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks) and [`IBM-Heron-156Q-Benchmarks`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks).

*(Metric note: The Studio UI field labeled `"State Fidelity [?]"` reports **Classical Computational-Basis Distribution Fidelity / Bhattacharyya overlap** $F_B = \sum_x \sqrt{P_{\text{ideal}}(x) P_{\text{meas}}(x)}$ ↑.)*

---

## 1. Three-Way Benchmark: 9Q Dense All-to-All ($K_9$, `ibm_marrakesh`, Job `dadl5jd1ierc738l1420`, `4,096` Shots)

Screenshots [`07`](../screenshots/07-qv-execution-result.png), [`08`](../screenshots/08-qv-hardware-allocation.png), [`09`](../screenshots/09-qv-circuit-structural-characteristics.png), and [`10`](../screenshots/10-qv-output-state-distribution.png):

| Metric | SABRE O3 | TKET | Prometheus | Prometheus vs. Best Baseline |
| :--- | ---: | ---: | ---: | ---: |
| **Circuit Depth (↓)** | 145 | 165 | **109** | **-24.83%** |
| **Two-Qubit `CZ` Gates (↓)** | 90 | 123 | **74** | **-17.78%** |
| **Distribution Fidelity $F_B$ (↑)** | 0.5738 | 0.5248 | **0.7466** | **+30.12%** |
| **Heavy-Output Probability HOP (↑)** | 0.6975 | 0.7339 | **0.8425** | **+14.80%** |
| **Total Variation Distance TVD (↓)** | 0.4572 | 0.5241 | **0.3015** | **-34.04%** |
| **Linear Cross-Entropy XEB (↑)** | 38.3213 | 31.1110 | **50.1079** | **+30.76%** |

---

## 2. Repeated-Execution Drift Controls: 9Q Dense All-to-All (`ibm_marrakesh`, `4,096` Shots)

Screenshots [`12`](../screenshots/12-dense-execution-drift-test1.png), [`13`](../screenshots/13-dense-execution-drift-test2.png), and [`14`](../screenshots/14-dense-execution-drift-test3.png):

| Control Run | IBM Quantum Job ID | Fidelity $F_B$ (`Baseline -> Prom` ↑) | HOP (`Baseline -> Prom` ↑) | TVD (`Baseline -> Prom` ↓) | XEB (`Baseline -> Prom` ↑) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Run 1 (`12`)** | `dacloht1ierc738jq1f0` | 0.6815 -> **0.7004** (`+2.77%`) | 0.8289 -> **0.8440** (`+1.83%`) | 0.3528 -> **0.3308** (`-6.23%`) | 11.4691 -> **13.0769** (`+14.02%`) |
| **Run 2 (`13`)** | `dacloslnj4cs73acqh90` | **0.7067** -> 0.6752 (`-4.45%`) | **0.8352** -> 0.8347 (`-0.06%`) | **0.3314** -> 0.3539 (`+6.79%`) | 12.4700 -> **12.7435** (`+2.19%`) |
| **Run 3 (`14`)** | `daclp3bdd5gc73d68lu0` | **0.7021** -> 0.6960 (`-0.86%`) | **0.8394** -> 0.8208 (`-2.21%`) | 0.3409 -> **0.3302** (`-3.13%`) | 12.2315 -> **13.0235** (`+6.48%`) |

---

## 3. Higher-Width (`12Q`-`16Q`) Dense All-to-All Comparisons (`15` - `18`)

| Comparison | Screenshot | Fidelity $F_B$ (`Base -> Prom` ↑) | HOP (`Base -> Prom` ↑) | TVD (`Base -> Prom` ↓) | XEB (`Base -> Prom` ↑) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Comparison 1 (`14Q`)** | [`15`](../screenshots/15-observed-gains-topology-comparison1.png) | 0.4353 -> **0.4778** (`+9.77%`) | 0.7515 -> **0.7839** (`+4.32%`) | 0.5812 -> **0.5345** (`-8.05%`) | 108.78 -> **120.79** (`+11.04%`) |
| **Comparison 2 (`16Q`)** | [`16`](../screenshots/16-observed-gains-topology-comparison2.png) | 0.5375 -> **0.5903** (`+9.83%`) | 0.7427 -> **0.7678** (`+3.39%`) | 0.4972 -> **0.4381** (`-11.88%`) | 17.61 -> **22.28** (`+26.55%`) |
| **Comparison 3 (`12Q`)** | [`17`](../screenshots/17-observed-gains-topology-comparison3.png), [`18`](../screenshots/18-observed-gains-topology-comparison3-depth-comparison.png) | 0.4268 -> **0.5656** (`+32.53%`) | 0.6736 -> **0.7358** (`+9.24%`) | 0.5967 -> **0.4620** (`-22.57%`) | 278.47 -> **400.51** (`+43.82%`) |

- **Screenshot [`18`](../screenshots/18-observed-gains-topology-comparison3-depth-comparison.png) Structural Comparison (Comparison 3, `12Q`):** Compiled Circuit Depth reduced from `199` to **`162`** (`-18.59%`), and Two-Qubit Gates reduced from `168` to **`137`** (`-18.45%`).
