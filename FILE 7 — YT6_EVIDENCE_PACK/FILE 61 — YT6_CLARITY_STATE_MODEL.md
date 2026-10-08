# YT6 Clarity State Model

The Clarity State Model defines the internal states YT6 transitions through during multi-turn clarity-layer execution.

## State Overview
YT6 operates across five clarity states:

1. Anchor State  
2. Structure State  
3. Tone State  
4. Reasoning State  
5. Validation State  

Each state enforces a different clarity-layer invariant.

## State 1 — Anchor State
Purpose:
- Normalise input
- Anchor context
- Prevent reinterpretation

Transitions to:
- Structure State

## State 2 — Structure State
Purpose:
- Apply deterministic formatting
- Enforce block layout

Transitions to:
- Tone State

## State 3 — Tone State
Purpose:
- Lock tone to neutral baseline
- Prevent emotional drift

Transitions to:
- Reasoning State

## State 4 — Reasoning State
Purpose:
- Align logical chains
- Maintain multi-turn coherence

Transitions to:
- Validation State

## State 5 — Validation State
Purpose:
- Validate reproducibility
- Confirm clarity invariants

Transitions to:
- Anchor State (cycle repeats)

The Clarity State Model defines YT6 as a state-driven clarity system.
