# Public Disclosure, Verification Tiers & Portfolio Scope

This portfolio hub ([`prometheus-execution-intelligence`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence)) indexes the 10 public quantum execution repositories published by Prometheus Dynamics Canada (`405` unique provider QPU Job/Task records across IBM Quantum, AWS Braket, and IQM Resonance; see [`PORTFOLIO_ACCOUNTING_LEDGER.json`](PORTFOLIO_ACCOUNTING_LEDGER.json) and `python scripts/verify_portfolio_accounting.py`).

## 1. Five Verification Tiers Across the Public Portfolio

Different repositories archive different levels of primary artifacts depending on payload size and IP boundaries. Readers and auditors should distinguish five distinct verification levels:

1. **Raw Measurement Histogram / `BitArray` Payload Reconstruction:**
   - Repositories archiving returned shot histograms or Qiskit `SamplerV2` `BitArray` payloads allow independent offline reconstruction of output probability distributions, Classical Bhattacharyya Overlap (`F_B`), Squared Hellinger Fidelity (`F_H = F_B²`), Total Variation Distance (`TVD`), task-specific observables, and (where physical OpenQASM circuits are included) compiled gate counts and depths:
     - [`AWS-Braket-Multi-Window-Validation`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation) (`450` circuits, raw shot counts + compiled QASM)
     - [`IBM-Heron-Extended-Validation-1023-Circuits`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits) (`1,023` circuits, raw measurement archives)
     - [`IQM-Resonance-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing) (`1,935` evaluations across `59` jobs, raw bitstring histograms)
     - [`IBM-Heron-156Q-Benchmarks`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks) (`144`-execution validation suite raw payloads + `297`-circuit tournament ledger)
     - [`qpu-selection-execution-quality`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality) (`33` archived IBM Quantum job ZIP bundles + `144`-execution suite)
     - [`prometheus-quantum-telemetry`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry) (`14` archived IBM `SamplerV2` result payloads)
2. **Outcome-Ledger Consistency, Billing Arithmetic & Statistical Recomputation:**
   - Repositories storing per-workload, per-subcircuit, and per-rung measured hardware outcomes (`fb_measured`, `fh_measured`, `tvd_measured`, `observable_measured`) without full `2^n` raw bitstring tables verify internal arithmetic (`F_H = F_B²`), dual-criteria acceptance rules, provider billing efficiency ratios (`billed seconds`, `active seconds`, `credits`), sequential stopping trajectories, paired Student-`t` / Wilcoxon / McNemar tests, cluster-robust variance estimators (`CRVE`), exact cluster sign-flip permutation tests, and Holm-Bonferroni multiplicity adjustments:
     - [`Prometheus-Quantum-Execution-Service`](https://github.com/PrometheusDynamicsCanada/Prometheus-Quantum-Execution-Service) (`157` provider records, `4,963` evaluations)
     - [`Quantum-Execution-Manager-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing) (`19` jobs, `1,140` evaluations)
     - [`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks) (`119` 3-way QPU jobs/tasks + `150` separate classical H100 GPU runs)
3. **Byte-Exact File Checksums (`REPO_SHA256_MANIFEST.json` & `REPOSITORY_SHA256SUMS.txt`):**
   - Checksum manifests verify that downloaded repository files match exact published `LF`-normalized Git archive bytes (`0` modifications after release packaging).
4. **Recorded SHA-256 References to Withheld Pre-Sanitization Artifacts:**
   - Where physical coordinate lists or internal scheduler columns are redacted for IP protection, fields such as `original_private_ledger_sha256` or `subgraph_sha256` preserve deterministic cryptographic references to private originals for continuity across files or confidential due-diligence audits; on their own in a public repository, they do not independently authenticate withheld private files.
5. **Local Runner Serialization Timestamps vs. Independent Pre-Submission Timestamping:**
   - Local JSON timestamp fields record runner serialization time on the benchmark host rather than third-party cryptographic timestamping before job submission (for example, [`AWS-Braket-Multi-Window-Validation`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation) explicitly discloses that Tasks 1-2 reflect later runner-resume commitment serialization, while Tasks 3-10 precede provider submission timestamps).

## 2. Withheld Proprietary Implementation & Clean-Repository Provenance

- **Withheld Internals:** Internal compiler routing heuristics, multi-objective scoring weights, structural Pareto selection rules, candidate-origin routing labels, numerical packing/stopping scheduler parameters, and internal fusion PINN equations are withheld across all public repositories.
- **Single-Commit Clean Repository Releases:** All public repositories in this portfolio are published as freshly initialized single-commit sanitized releases with isolated Git object histories (`0` historical pre-sanitization commits in repository object storage). Note that external copies downloaded prior to repository recreation cannot be recalled.
