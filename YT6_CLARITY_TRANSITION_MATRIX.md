# YT6 — Clarity Transition Matrix

This document defines the transition matrix governing clarity-state movement within the YT6 system.

## Matrix Axis A — Intention State Transitions
From INT-BASE:
- to ACT-READY
- to LB-STABLE

From INT-LOCK:
- to ACT-EXEC
- to REF-BASE

From INT-SHIFT:
- to ACT-READY
- to LB-FOOTPRINT

## Matrix Axis B — Action State Transitions
From ACT-READY:
- to ACT-EXEC
- to SYM-LOCK

From ACT-EXEC:
- to REF-BASE
- to REF-STABLE

From ACT-CHAIN:
- to REF-STABLE
- to CAR-FLOW

## Matrix Axis C — Reflection State Transitions
From REF-BASE:
- to INT-LOCK
- to SYM-ANCHOR

From REF-STABLE:
- to INT-BASE
- to LB-STABLE

From REF-DRIFT:
- to CAR-BREAK
- to SYM-DRIFT

## Matrix Axis D — Symbol State Transitions
From SYM-LOCK:
- to ACT-EXEC
- to REF-STABLE

From SYM-ANCHOR:
- to ACT-CHAIN
- to REF-BASE

From SYM-DRIFT:
- to CAR-BREAK
- to INT-SHIFT

## Matrix Axis E — Lifebox State Transitions
From LB-STABLE:
- to INT-BASE
- to REF-STABLE

From LB-FOOTPRINT:
- to INT-LOCK
- to REF-BASE

From LB-NEUTRAL:
- to INT-BASE
- to CAR-FLOW

## Matrix Axis F — CAR Loop State Transitions
From CAR-START:
- to CAR-FLOW

From CAR-FLOW:
- to INT-BASE

From CAR-BREAK:
- to REF-DRIFT
- to SYM-DRIFT

This matrix defines clarity-state transitions within YT6.
