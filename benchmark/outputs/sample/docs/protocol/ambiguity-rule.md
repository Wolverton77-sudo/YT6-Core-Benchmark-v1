# YT6 Ambiguity Rule

The ambiguity rule prevents drift, invention, and semantic mutation inside YT6.

## 1. Core Principle
If required information is missing, undefined, conflicting, or unavailable:

**The agent must not invent meaning.**

## 2. Required Behaviour
When ambiguity is detected, the agent must:

1. **Mark the ambiguity explicitly**  
   Example: "Ambiguity detected: missing parameter X."

2. **Request the minimum missing detail**  
   Only the smallest piece of information required to continue.

3. **Preserve Base44 semantics**  
   No symbol meaning may change under ambiguity.

4. **Maintain intention continuity**  
   The agent must not shift purpose or goal.

## 3. Prohibited Behaviour
- Guessing  
- Assuming  
- Inventing new meaning  
- Mutating Base44 symbols  
- Changing task intention  

## 4. Purpose
This rule ensures:
- stability  
- reproducibility  
- clarity under load  
- drift‑resistance  
- deterministic behaviour  

This is a mandatory rule for all YT6‑compliant agents.
