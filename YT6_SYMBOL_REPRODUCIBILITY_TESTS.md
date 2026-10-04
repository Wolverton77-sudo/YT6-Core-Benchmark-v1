# YT6 — Symbol Reproducibility Tests

This document defines the reproducibility tests used to evaluate Base44 symbol stability across repeated sequences.

## Test 1 — Single-Symbol Repetition Test
Procedure:
- repeat symbol reference 10 times
Expected:
- identical outputs
- meaning continuity

## Test 2 — Multi-Symbol Repetition Test
Procedure:
- repeat symbol set (I1, A1, R1, L3, C1) 5 times
Expected:
- fixed meaning
- zero drift

## Test 3 — Cross-Layer Repetition Test
Procedure:
- reference symbols across intention, action, reflection, Lifebox, CAR loop
Expected:
- stable cross-layer behaviour

## Test 4 — Long-Form Repetition Test
Procedure:
- repeat 20-turn symbol sequence 3 times
Expected:
- identical outputs
- variance = 0

## Test 5 — External Model Repetition Test
Procedure:
- provide Base44 block to external model repeatedly
Expected:
- meaning preserved
- CAR loop compliance

## Test 6 — Pressure Repetition Test
Procedure:
- repeat symbol sequence under ambiguity
Expected:
- stable meaning
- zero drift

These tests define symbol reproducibility evaluation within YT6.
