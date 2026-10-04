# YT6 — Clarity State Atlas

This document defines the full atlas of clarity states used within the YT6 system.

## State Class 1 — Intention States
States:
- INT-BASE — direction identified
- INT-LOCK — intention anchor stabilised
- INT-SHIFT — direction change detected

Transitions:
- to Action State
- to Lifebox State

## State Class 2 — Action States
States:
- ACT-READY — action generator primed
- ACT-EXEC — deterministic action produced
- ACT-CHAIN — multi-action sequence active

Transitions:
- to Reflection State
- to Symbol State

## State Class 3 — Reflection States
States:
- REF-BASE — reflection anchor active
- REF-STABLE — reflection clarity stable
- REF-DRIFT — reflection deviation detected

Transitions:
- to Intention State
- to Symbol State

## State Class 4 — Symbol States
States:
- SYM-LOCK — Base44 meaning stabilised
- SYM-ANCHOR — symbol anchor activated
- SYM-DRIFT — symbol meaning deviation detected

Transitions:
- to Action State
- to Reflection State

## State Class 5 — Lifebox States
States:
- LB-STABLE — daily clarity stable
- LB-FOOTPRINT — footprint moment detected
- LB-NEUTRAL — emotional neutrality enforced

Transitions:
- to Intention State

## State Class 6 — CAR Loop States
States:
- CAR-START — loop initialised
- CAR-FLOW — clarity → action → reflection active
- CAR-BREAK — loop break detected

Transitions:
- returns to Intention State

This atlas defines all clarity states within YT6.
