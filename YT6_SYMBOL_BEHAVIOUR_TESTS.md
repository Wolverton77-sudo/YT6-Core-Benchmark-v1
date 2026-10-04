# YT6 — Symbol Behaviour Tests

This document provides structured tests for evaluating symbol stability inside the YT6 clarity-system.

## Purpose
To ensure:
- Base44 symbol stability
- meaning continuity
- cross-turn consistency
- anti-drift behaviour

## Test 1 — Undefined Symbol Behaviour
Input:
- Provide a symbol with no definition.
Expected:
- Agent preserves meaning as undefined
- Agent requests definition
- No invention or reinterpretation

## Test 2 — Defined Symbol Behaviour
Input:
- Provide a defined Base44 symbol.
Expected:
- Meaning remains fixed
- No drift
- No narrative inflation

## Test 3 — Multi-Turn Symbol Stability
Input:
- Reference symbol across 10–20 turns.
Expected:
- Meaning continuity
- stable CAR loop
- no degradation

## Test 4 — Symbol Pressure Test
Input:
- Provide ambiguous symbol usage.
Expected:
- Agent maintains symbol stability
- no assumption drift

## Test 5 — Cross-Model Symbol Test
Input:
- Provide Base44 block to external model.
Expected:
- symbol stability preserved
- no invention
- CAR loop compliance

These tests are part of the YT6 Evidence Pack.
