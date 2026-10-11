# YT6 Agent Integration Example

This page shows how an AI agent integrates YT6 clarity rules, Base44 semantics, and the clarity spine.

## 1. Initialise the Agent
The agent must load:
- Base44 symbol meanings
- YT6 core rules
- Ambiguity rule
- Clarity spine (Clarity → Action → Reflection)

## 2. Apply Base44 Semantics
Example:
- `M1` = meaning anchor
- `S1` = stability anchor
- `R1` = reproducibility anchor
- `C1` = continuity anchor

These meanings must remain fixed.

## 3. Apply the Clarity Spine
Every agent turn follows:

### Clarity
State intention, constraints, and required information.

### Action
Execute the task with stability and no drift.

### Reflection
State what changed, what stayed stable, and whether ambiguity occurred.

## 4. Ambiguity Handling
If the agent lacks information:
- mark ambiguity
- request minimum missing detail
- preserve Base44 meanings
- continue intention

## 5. Example Integration Snippet (Pseudo‑Code)
