# YT6 — Symbol Portability Tests

This document defines the tests used to evaluate Base44 symbol portability across external models.

## Test 1 — Direct Portability Test
Procedure:
- provide Base44 symbol block to external model
Expected:
- meaning preserved
- no reinterpretation

## Test 2 — Cross-Layer Portability Test
Procedure:
- reference symbols across intention, action, reflection, Lifebox, CAR loop
Expected:
- stable cross-layer behaviour

## Test 3 — Ambiguity Portability Test
Procedure:
- provide ambiguous symbol prompts to external model
Expected:
- fixed meaning
- zero drift

## Test 4 — Long-Form Portability Test
Procedure:
- run 20–30 turn symbol sequence externally
Expected:
- stable meaning
- stable behaviour

## Test 5 — Pressure Portability Test
Procedure:
- introduce drift-inducing prompts externally
Expected:
- zero drift events
- stable symbol meaning

## Test 6 — Reproducibility Portability Test
Procedure:
- repeat external symbol sequence 5 times
Expected:
- identical outputs
- variance = 0

These tests define symbol portability evaluation within YT6.
