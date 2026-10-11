# YT6 — Execution Trace Format (Tier‑5)

Execution traces record every clarity decision made during runtime.

---

## 1. Purpose
Execution traces provide:
- full transparency  
- reproducibility  
- drift detection  
- ambiguity tracking  
- stability verification  

---

## 2. Trace Structure
Each trace contains:

### 1. Clarity Phase Trace
- intention  
- constraints  
- ambiguity status  
- Base44 lock status  

### 2. Action Phase Trace
- execution steps  
- stability behaviour  
- drift behaviour  

### 3. Reflection Phase Trace
- stable elements  
- changed elements  
- ambiguity resolution  
- drift status  

### 4. Telemetry Snapshot
- clarity score  
- drift score  
- ambiguity score  
- stability score  
- continuity score  

---

## 3. Trace Format (Structured)
