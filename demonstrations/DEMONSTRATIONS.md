# Studio Interface Walkthrough

Index of the 18 Prometheus Studio screenshots stored in [`../screenshots/`](../screenshots/).

*(Note: Filenames `07-qv-*` through `10-qv-*` are preserved for link compatibility; screenshots `07`-`10` show the **9-Qubit Dense All-to-All ($K_9$)** 3-way benchmark `dadl5jd1ierc738l1420` on `ibm_marrakesh`, and screenshot `11` shows **8-Qubit Quantum Volume (`Random SU(4)`)** `dabeu63vpcac73ddn40g` on `ibm_kingston`.)*

---

## 1. Workload & Target Configuration (`01` - `06`)
- [`01-studio-overview.png`](../screenshots/01-studio-overview.png) - Main Prometheus Studio dashboard and telemetry controls.
- [`02-target-processor.png`](../screenshots/02-target-processor.png) - Target QPU and multi-processor broadcast selection.
- [`03-workload-family.png`](../screenshots/03-workload-family.png) - Benchmark circuit family selector.
- [`04-search-budget.png`](../screenshots/04-search-budget.png) - Candidate search budget configuration.
- [`05-shot-count.png`](../screenshots/05-shot-count.png) - Hardware shot-count selection.
- [`06-logical-qasm.png`](../screenshots/06-logical-qasm.png) - OpenQASM 2.0 logical circuit input panel.

---

## 2. 9Q Dense All-to-All 3-Way Benchmark (`dadl5jd1ierc738l1420`) & 8Q Quantum Volume (`dabeu63vpcac73ddn40g`) (`07` - `11`)
- [`07-qv-execution-result.png`](../screenshots/07-qv-execution-result.png) - **9Q Dense All-to-All (`ibm_marrakesh`, `dadl5jd1ierc738l1420`, `4,096` shots):** 3-way measured execution results (`SABRE O3` `0.5738` vs. `TKET` `0.5248` vs. `Prometheus` **`0.7466`**, `+30.12%`).
- [`08-qv-hardware-allocation.png`](../screenshots/08-qv-hardware-allocation.png) - **9Q Dense All-to-All (`ibm_marrakesh`, `dadl5jd1ierc738l1420`):** Physical 156-qubit topology allocation view (public release redaction).
- [`09-qv-circuit-structural-characteristics.png`](../screenshots/09-qv-circuit-structural-characteristics.png) - **9Q Dense All-to-All (`ibm_marrakesh`, `dadl5jd1ierc738l1420`):** Compiled depth (`145 / 165 /` **`109`**) and two-qubit gate (`90 / 123 /` **`74`**) comparison.
- [`10-qv-output-state-distribution.png`](../screenshots/10-qv-output-state-distribution.png) - **9Q Dense All-to-All (`ibm_marrakesh`, `dadl5jd1ierc738l1420`):** Measured 3-compiler Z-basis bitstring probability distribution.
- [`11-qv-logical-compiled-qasm.png`](../screenshots/11-qv-logical-compiled-qasm.png) - **8Q Quantum Volume (`ibm_kingston`, `dabeu63vpcac73ddn40g`, `4,096` shots):** Logical OpenQASM 2.0 inspection view.

---

## 3. Dense All-to-All Repeated-Run Controls & Higher-Width (`12Q`-`16Q`) Comparisons (`12` - `18`)
- [`12-dense-execution-drift-test1.png`](../screenshots/12-dense-execution-drift-test1.png) - 9Q Dense All-to-All repeated-execution control 1 (`ibm_marrakesh`, `dacloht1ierc738jq1f0`, `4,096` shots).
- [`13-dense-execution-drift-test2.png`](../screenshots/13-dense-execution-drift-test2.png) - 9Q Dense All-to-All repeated-execution control 2 (`ibm_marrakesh`, `dacloslnj4cs73acqh90`, `4,096` shots).
- [`14-dense-execution-drift-test3.png`](../screenshots/14-dense-execution-drift-test3.png) - 9Q Dense All-to-All repeated-execution control 3 (`ibm_marrakesh`, `daclp3bdd5gc73d68lu0`, `4,096` shots).
- [`15-observed-gains-topology-comparison1.png`](../screenshots/15-observed-gains-topology-comparison1.png) - Higher-width Dense All-to-All comparison 1 (`+9.77%` Distribution Fidelity $F_B$).
- [`16-observed-gains-topology-comparison2.png`](../screenshots/16-observed-gains-topology-comparison2.png) - Higher-width Dense All-to-All comparison 2 (`+9.83%` Distribution Fidelity $F_B$, `+26.55%` XEB).
- [`17-observed-gains-topology-comparison3.png`](../screenshots/17-observed-gains-topology-comparison3.png) - 12Q Dense All-to-All comparison 3 on `ibm_marrakesh` (`+32.53%` Distribution Fidelity $F_B$, `+43.82%` XEB).
- [`18-observed-gains-topology-comparison3-depth-comparison.png`](../screenshots/18-observed-gains-topology-comparison3-depth-comparison.png) - 12Q Dense All-to-All comparison 3 structural depth (`-18.59%`) and 2Q gate (`-18.45%`) reduction.
