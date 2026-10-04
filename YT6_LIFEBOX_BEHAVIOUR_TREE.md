# YT6 — Lifebox Behaviour Tree

This document defines the behaviour tree used to evaluate Lifebox clarity behaviour.

## Root Node — Daily Clarity State
Question:
- Is daily clarity stable?

If YES → proceed to Footprint Node  
If NO → classify as Daily Clarity Drift

---

## Node 1 — Footprint Moment Node
Question:
- Is a footprint moment detected?

If YES → proceed to Neutrality Node  
If NO → classify as Footprint Detection Failure

---

## Node 2 — Emotional Neutrality Node
Question:
- Is emotional neutrality maintained?

If YES → proceed to Long-Form Node  
If NO → classify as Emotional Drift

---

## Node 3 — Long-Form Stability Node
Question:
- Is clarity stable across extended sequences?

If YES → proceed to Reproducibility Node  
If NO → classify as Long-Form Drift

---

## Node 4 — Reproducibility Node
Question:
- Are repeated scenarios identical?

If YES → classify as Full Lifebox Stability  
If NO → classify as Lifebox Reproducibility Failure

---

## Behaviour Outcomes
- Daily Clarity Drift  
- Footprint Detection Failure  
- Emotional Drift  
- Long-Form Drift  
- Lifebox Reproducibility Failure  
- Full Lifebox Stability

This behaviour tree defines Lifebox evaluation within YT6.
