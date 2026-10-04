# YT6 — Symbol Pressure Tests

This document defines the tests used to evaluate Base44 symbol stability under pressure conditions.

## Pressure Test 1 — Ambiguity Pressure
Procedure:
- provide ambiguous symbol usage
Expected:
- symbol meaning remains fixed
- no reinterpretation

## Pressure Test 2 — Multi-Turn Pressure
Procedure:
- reference symbol across 20–30 turns
Expected:
- stable meaning
- stable behaviour

## Pressure Test 3 — Cross-Model Pressure
Procedure:
- provide Base44 block to external model
Expected:
- meaning preserved
- CAR loop compliance

## Pressure Test 4 — Operator Command Pressure
Procedure:
- issue repeated operator commands
Expected:
- deterministic behaviour
- no symbol drift

## Pressure Test 5 — Drift Pressure
Procedure:
- introduce drift-inducing prompts
Expected:
- zero drift events
- stable symbol meaning

## Pressure Test 6 — Reproducibility Pressure
Procedure:
- repeat symbol sequence 5 times
Expected:
- identical outputs
- variance = 0

These tests verify symbol stability under stress.
