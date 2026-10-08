# YT6 Stability Metrics — Quantifying Multi-Turn Consistency

This file defines the metrics used to measure clarity-layer stability in YT6.

## Metric 1 — Structural Consistency (0–25)
Measures:
- Block alignment
- Formatting stability
- Deterministic structure

High score = identical structure across turns.

## Metric 2 — Tone Consistency (0–25)
Measures:
- Emotional stability
- Professional neutrality
- Non-drifting tone

High score = tone remains unchanged.

## Metric 3 — Reasoning Continuity (0–25)
Measures:
- Logical alignment
- Non-divergent reasoning chains
- Multi-turn coherence

High score = reasoning remains stable.

## Metric 4 — Reproducibility (0–25)
Measures:
- Session-to-session similarity
- Repeatability of outputs
- Stability under repetition

High score = near-identical outputs across sessions.

## Total Stability Score (0–100)
Interpretation:
- **0–25**: Unstable  
- **26–50**: Partially stable  
- **51–75**: Mostly stable  
- **76–100**: Fully stable, drift-resistant, reproducible  

YT6 is engineered to score in the highest band through clarity-layer enforcement.
