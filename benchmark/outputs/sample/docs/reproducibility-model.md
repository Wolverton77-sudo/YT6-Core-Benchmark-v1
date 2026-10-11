# YT6 Reproducibility Model

The YT6 benchmark is designed to be fully reproducible across environments, agents, and evaluation runs.

## 1. Deterministic Inputs
All benchmark inputs are fixed:
- tasks.yaml
- drift-tests.yaml
- ambiguity-tests.yaml

These files define the exact sequences used in every run.

## 2. Deterministic Outputs
Each run produces:
- run-summary.json
- telemetry.json (optional future extension)
- traces.json (optional future extension)

Outputs follow a strict schema to ensure comparability.

## 3. Scoring Rules
Scoring is defined in:
- benchmark/scoring/scoring_rules.yaml

Metrics:
- drift score
- clarity score
- ambiguity handling score
- reflection accuracy

## 4. Ambiguity Rule
YT6 agents must not invent meaning when information is missing.
They must:
1. mark the ambiguity,
2. request the minimum missing detail,
3. preserve Base44 semantics.

## 5. Baseline Comparison
A baseline agent (non-YT6) is run using:
- run_baseline.py

This allows direct comparison between YT6 and standard behaviour.

## 6. Verification
A run is reproducible if:
- inputs match the repo versions,
- outputs follow the schema,
- scoring is consistent,
- baseline comparison is available.

This model ensures YT6 clarity behaviour is testable, inspectable, and repeatable.
