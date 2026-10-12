# YT6 Benchmark Evaluation

This document explains how the YT6 benchmark suite is evaluated.

## 1. Purpose
The benchmark measures:
- clarity stability
- drift resistance
- deterministic behaviour
- operator correctness
- reproducibility

## 2. Components
The benchmark uses:
- Field
- Frame
- Fieldframe
- Prime
- Primeframe
- DeterministicOperator
- DriftResistantOperator
- ClarityEnforcer

## 3. Task Structure
Each task contains:
- USER input
- SYSTEM output
- metadata

## 4. Evaluation Outputs
Each task produces:
- clarity signals
- deterministic decision
- drift assessment
- clarity enforcement decision

## 5. Snapshot
The final benchmark snapshot is written to:
`benchmark/results/snapshot.md`
