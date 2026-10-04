# YT6 — Clarity State Machine

This document defines the state machine that governs clarity transitions within the YT6 system.

## State 1 — Intention State
Description:
- user direction identified
- intention anchor set

Transitions:
- to Action State when next move required

## State 2 — Action State
Description:
- deterministic next action produced
- operator-grade clarity active

Transitions:
- to Reflection State after action delivered

## State 3 — Reflection State
Description:
- clarity evolution stabilised
- reflection anchor set

Transitions:
- to Intention State when new direction appears
- to Symbol State when symbol referenced

## State 4 — Symbol State
Description:
- Base44 meaning stabilised
- symbol anchor activated

Transitions:
- to Action State if symbol triggers operator command
- to Reflection State if symbol clarifies meaning

## State 5 — Lifebox State
Description:
- daily clarity stabilised
- footprint moment anchored

Transitions:
- to Intention State when daily clarity shifts
- to Reflection State when stability changes

## State 6 — CAR Loop State
Description:
- clarity → action → reflection cycle active

Transitions:
- loops internally unless drift detected
- returns to Intention State after cycle completes

This state machine defines clarity transitions in YT6.
