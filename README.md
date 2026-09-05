# PROMETHEUS // Quantum Execution Intelligence

**Hardware-aware quantum execution intelligence for evaluating, selecting, and dispatching quantum workloads across compilers and heterogeneous QPUs.**

Prometheus sits above the compilation layer and evaluates how a workload should actually execute on available quantum hardware.

Instead of treating a single compiler output as the final answer, Prometheus can evaluate multiple valid execution candidates, characterize the hardware environment, compare execution trajectories, and select the candidate and physical execution environment most appropriate for the workload.

---

## The Problem

Quantum compilers are extremely good at producing valid physical circuits.

But a valid circuit is not necessarily the best circuit to execute on a real QPU.

Physical processors are heterogeneous.

Gate errors, readout behavior, connectivity, calibration conditions, local hardware quality, and short-timescale variation can differ substantially across a processor.

The same logical workload can therefore produce different execution quality depending on:

- which compiler generated the circuit;
- which routing strategy was used;
- which physical qubits were selected;
- which QPU receives the workload;
- and the hardware state at execution time.

Prometheus is designed to make that decision explicitly.

---

# What Prometheus Does

Prometheus provides a hardware-aware execution layer between quantum workloads and quantum processors.

At a high level:

    Quantum Workload
           │
           ▼
    Candidate Generation
           │
           ├──────────────┐
           │              │
           ▼              ▼
       SABRE O3          TKET
           │              │
           └──────┬───────┘
                  │
                  ▼
        Execution Candidates
                  │
                  ▼
       Current Hardware State
                  │
                  ▼
       Hardware-Aware Evaluation
                  │
                  ▼
        Execution Selection
                  │
                  ▼
          QPU Selection
                  │
                  ▼
             Job Dispatch
                  │
                  ▼
        Observed Execution
                  │
                  ▼
       Telemetry / Drift Data

The key distinction is:

**Compilation generates candidates. Prometheus evaluates which candidate should actually execute.**

---

# Multi-Compiler Execution

Prometheus is designed to be compiler-agnostic.

Current candidate-generation integrations include:

- **SABRE O3 / Qiskit**
- **TKET**
- Prometheus hardware-aware candidate generation and optimization
- additional compilation strategies as the system expands

Rather than replacing existing compiler infrastructure, Prometheus can treat compiler outputs as alternative execution candidates.

This allows different compilation strategies to be evaluated against the same hardware conditions and workload.

The question becomes:

> **Which valid execution should actually reach the QPU?**

---

# Hardware-Aware Execution

Prometheus evaluates execution candidates against physical hardware information rather than relying solely on abstract circuit cost.

The system can incorporate hardware characteristics including:

- two-qubit gate error;
- readout error;
- physical connectivity;
- qubit availability;
- local hardware quality;
- calibration state;
- execution conditions;
- circuit structure;
- routing overhead;
- measured execution outcomes.

The objective is not simply to minimize gate count.

The objective is to identify an execution that is appropriate for the physical environment in which it will run.

---

# Multi-QPU Arbitration

Prometheus can evaluate workloads across multiple operational QPUs.

This enables workload-specific processor selection rather than relying exclusively on a permanent global ranking of available machines.

A workload can therefore be evaluated against:

**Workload → Compiler → Physical Mapping → QPU**

rather than:

**Workload → Default Compiler → Default QPU**

This creates the foundation for execution-aware quantum fleet management.

---

# Current Demonstrated System

The current system provides an operational environment for:

- quantum workload configuration;
- IBM Quantum processor discovery;
- hardware characterization;
- SABRE O3 candidate generation;
- TKET candidate generation;
- multi-compiler comparison;
- hardware-aware execution evaluation;
- physical candidate selection;
- cross-QPU arbitration;
- real hardware dispatch;
- comparative execution;
- execution telemetry;
- result inspection;
- hardware/run variability observation.

---

# Comparative Execution

Prometheus can compare execution candidates using measured and hardware-aware indicators including:

- State Fidelity
- Heavy Output Probability (HOP)
- Total Variation Distance (TVD)
- Cross-Entropy / XEB
- two-qubit gate count
- physical circuit depth
- routing overhead
- hardware-weighted execution cost
- hardware allocation
- output-state distributions
- execution metadata

The system can retain a baseline execution when an alternative does not provide a sufficiently favorable outcome.

Prometheus does not need to intervene simply because an alternative exists.

---

# Real Hardware

Prometheus has been developed and tested using real IBM Quantum hardware.

Representative work includes IBM Heron processors and comparative execution across multiple workloads and hardware conditions.

A representative IBM Marrakesh execution demonstrated:

- **43.02% displayed execution-cost reduction**
- State Fidelity: **0.6815 → 0.7004**
- Heavy Output Probability: **0.8289 → 0.8440**
- TVD: **0.3528 → 0.3308**
- XEB: **11.4691 → 13.0769**

These values are representative experimental observations, not a universal performance guarantee.

---

# Why This Matters

Traditional compilation asks:

> **How do I produce a valid circuit for this QPU?**

Prometheus asks:

> **Which valid physical execution is most appropriate for this workload, this hardware, and this execution environment?**

That distinction becomes increasingly important as quantum processors become larger, more heterogeneous, and more numerous.

A quantum workload should not necessarily be permanently tied to:

- one compiler;
- one routing strategy;
- one physical region;
- or one QPU.

Prometheus is designed to provide the decision layer between those components.

---

# Architecture

The system separates four major responsibilities:

### 1. Candidate Generation

Existing compilers and routing systems produce valid physical execution candidates.

Current integrations include:

- SABRE O3 / Qiskit
- TKET
- Prometheus optimization

### 2. Hardware Characterization

Prometheus gathers information about the current physical execution environment.

### 3. Execution Arbitration

Candidate executions are evaluated against the hardware environment and workload requirements.

The proprietary execution-selection mechanism is not disclosed in this repository.

### 4. Dispatch

The selected execution candidate and QPU are dispatched for real execution.

Observed results can then be retained as execution telemetry and used to study hardware/run variation.

---

# Prometheus Is Not a Replacement for SABRE or TKET

Prometheus does not need to replace existing compilation infrastructure.

SABRE, TKET, Qiskit, and other compilation systems can remain responsible for generating high-quality physical circuit candidates.

Prometheus operates at a different layer.

Their outputs become candidates.

**Prometheus decides which candidate should execute.**

This creates a compiler-agnostic execution architecture in which multiple compilation strategies can compete against the same physical hardware conditions.

---

# Research Direction

The longer-term objective is a multi-compiler, multi-QPU execution-intelligence and dispatch layer.

The architecture is intended to expand across:

- additional compilation frameworks;
- additional IBM Quantum processors;
- Quantinuum;
- IonQ;
- other quantum providers;
- superconducting processors;
- trapped-ion processors;
- other emerging quantum processor architectures.

The underlying abstraction is intentionally broader than any single compiler or hardware technology.

---

# Practical Applications

Prometheus can provide infrastructure for:

### Quantum Fleet Management

Workload-specific QPU selection and execution-aware dispatch.

### Compiler Enhancement

Evaluate multiple compiler trajectories without replacing existing compilation infrastructure.

### Hardware-Aware Compilation

Select physical executions according to the hardware environment rather than topology alone.

### Multi-Vendor Execution

Provide a common execution-arbitration abstraction across different quantum processor technologies.

### Enterprise Quantum Workloads

Add execution selection, dispatch, execution history, and hardware/run observation between applications and quantum processors.

### Quantum Benchmarking

Compare compiler strategies, QPUs, workloads, calibration states, routing strategies, and observed execution quality.

---

# Public Disclosure

This repository is a public capability record and architectural demonstration.

### Public

- system workflow;
- architecture;
- interface screenshots;
- compiler integration concepts;
- representative execution outcomes;
- hardware observations;
- research direction;
- demonstration results.

### Controlled

- proprietary implementation;
- proprietary equations and derivations;
- feature construction;
- internal weights and coefficients;
- internal ranking;
- detailed selection heuristics;
- private infrastructure.

The repository intentionally does not contain the complete chain required to reconstruct the proprietary execution-selection mechanism.

---

# Important Scope

Prometheus does **not** claim:

- universal superiority over every compiler;
- improved fidelity on every workload;
- a universal optimum across all QPUs;
- that routing cost is irrelevant;
- that one compiler should always be selected;
- that every planned hardware integration is currently operational.

The purpose of the system is to make execution decisions based on measured and modeled hardware conditions and to validate those decisions experimentally.

Neutral and unfavorable outcomes are valuable because they define the operating envelope of the system.

---

# Core Concept

Prometheus turns quantum execution into a decision problem.

Instead of:

    Workload
       ↓
    Compiler
       ↓
    QPU

Prometheus enables:

    Workload
       ↓
    Multiple Candidates
       ↓
    Hardware Characterization
       ↓
    Execution Intelligence
       ↓
    Compiler / Circuit / QPU Selection
       ↓
    Dispatch
       ↓
    Measured Execution
       ↓
    Telemetry

**Generate multiple valid possibilities.**

**Understand the hardware.**

**Select the execution.**

**Measure what happened.**

---

## Prometheus Dynamics

Prometheus is being developed as a quantum execution-intelligence layer for hardware-aware compilation, routing, QPU selection, and execution.

**Website:** https://prometheusdynamics.ca

**Organization:** https://github.com/PrometheusDynamicsCanada
