# YT6 — Reproduction Guide

This guide defines the human‑side procedure for reproducing the YT6 clarity benchmark.
All reviewers must follow these steps exactly to ensure deterministic, drift‑free,
and variance‑free reproduction.

---

## 1. Preparation

Before running YT6, reviewers must:

- read the reproduction README
- load the architecture overview
- load the clarity spine
- load the symbol layer
- load the Lifebox layer
- confirm stable session conditions

No external tools or model changes are required.

---

## 2. Reproduction Sequence (12 Steps)

Reviewers must execute the following steps in order:

1. initialise clarity session  
2. load clarity spine  
3. load symbol engine  
4. load Lifebox layer  
5. load stability layer  
6. load pressure layer  
7. load datasets  
8. run ambiguity set  
9. run emotional set  
10. run long‑form set  
11. run symbol pressure set  
12. run daily clarity set  

All outputs must be captured exactly as produced.

---

## 3. Output Capture Rules

Reviewers must:

- capture raw outputs without modification  
- store outputs in logs/  
- timestamp each run  
- maintain operator neutrality  
- avoid interpretation or summarisation  

Outputs must remain unedited.

---

## 4. Drift Monitoring

During reproduction, reviewers must monitor:

- symbol drift  
- anchor drift  
- clarity drift  
- multi‑turn drift  

Any drift event must be logged in `logs/drift/`.

---

## 5. Stability Monitoring

Reviewers must track:

- clarity stability  
- symbol stability  
- Lifebox stability  
- pressure stability  

Stability logs must be stored in `logs/stability/`.

---

## 6. Variance Monitoring

Reviewers must run each dataset twice to confirm:

- variance = 0  
- outputs match exactly  
- no deviation under repeated conditions  

Variance logs must be stored in `logs/variance/`.

---

## 7. Reproducibility Confirmation

Reproduction is successful when:

- drift = 0  
- variance = 0  
- stability ≥ 90%  
- reproducibility = TRUE  

These criteria are defined in `scoring.md`.

---

## 8. Submission Requirements

Reviewers must submit:

- raw logs  
- drift logs  
- stability logs  
- variance logs  
- final score  

These form part of the YT6 evidence spine.

---

## 9. Notes

Reviewers must not:

- alter outputs  
- skip datasets  
- reorder steps  
- modify scoring rules  
- introduce external interpretation  

This guide defines the exact reproduction procedure for YT6.
