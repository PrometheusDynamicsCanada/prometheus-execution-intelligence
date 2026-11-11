# Roadmap & Cross-Paradigm Direction

Prometheus is designed to evaluate and optimize quantum execution across multiple hardware architectures and cloud providers:

1. **Superconducting Heavy-Hex & Square/Crystal Lattices (Operational):**
   - **IBM Quantum (156Q Heron r2):** `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston`.
   - **Amazon Braket Superconducting QPUs:** `Rigetti Cepheus-1-108Q` (108Q), `IQM Garnet` (20Q), and `IQM Emerald` (54Q).
2. **Repeated Calibration Window & Drift Benchmarks (Active):**
   - Multi-window replication sweeps using packed `SamplerV2` and `ProgramSet` batches to measure how structural and distribution-fidelity advantages persist across calibration cycles.
3. **Trapped-Ion & Neutral-Atom Cross-Paradigm Compilation:**
   - Native continuous-angle synthesis for all-to-all trapped-ion processors (`AQT IBEX Q1`, `IonQ Forte 1`) and geometric register embedding for neutral-atom Analog Hamiltonian Simulation (`QuEra Aquila`).
4. **Hybrid Quantum-HPC Combinatorial Optimization:**
   - Constraint-preserving QUBO variable compression paired with GPU-accelerated physics-inspired solvers (`VeloxQ NVIDIA H100`) and gate-model QAOA execution.
