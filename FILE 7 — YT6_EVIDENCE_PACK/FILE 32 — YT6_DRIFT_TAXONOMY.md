# YT6 Drift Taxonomy — Classification of Drift Behaviours

This file defines the taxonomy of drift behaviours observed in multi-turn AI systems.

## Category 1 — Tone Drift
Definition:
Unintended changes in emotional style or personality.

Examples:
- Neutral → enthusiastic
- Professional → casual
- Direct → verbose

YT6 Countermeasure:
Tone locking.

## Category 2 — Structural Drift
Definition:
Changes in formatting, layout or block structure.

Examples:
- Loss of headings
- Random paragraph shifts
- Inconsistent list formatting

YT6 Countermeasure:
Deterministic structure enforcement.

## Category 3 — Reasoning Drift
Definition:
Divergence in logic, conclusions or reasoning chains.

Examples:
- Contradicting earlier statements
- Changing interpretation of context
- Losing multi-turn alignment

YT6 Countermeasure:
Reasoning continuity rules.

## Category 4 — Context Drift
Definition:
Misalignment or reinterpretation of earlier turns.

Examples:
- Forgetting constraints
- Reinterpreting instructions
- Shifting conversation goals

YT6 Countermeasure:
Context anchoring.

## Category 5 — Output Drift
Definition:
Changes in output style, density or clarity.

Examples:
- Sudden verbosity
- Sudden minimalism
- Unpredictable formatting

YT6 Countermeasure:
Clarity-layer invariants.

This taxonomy is used in YT6 benchmarking and evidence analysis.
