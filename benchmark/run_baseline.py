#!/usr/bin/env python3

"""
YT6 Baseline Runner
Runs a non-YT6 agent for comparison against the YT6 benchmark.
This establishes drift, clarity, and ambiguity differences.
"""

import json
import datetime
from pathlib import Path

def load_inputs():
    with open("benchmark/inputs/tasks.yaml", "r") as f:
        tasks = f.read()
    with open("benchmark/inputs/drift-tests.yaml", "r") as f:
        drift = f.read()
    with open("benchmark/inputs/ambiguity-tests.yaml", "r") as f:
        ambiguity = f.read()
    return tasks, drift, ambiguity

def run_baseline_agent(task):
    # Placeholder baseline behaviour (non-YT6)
    return {
        "input": task,
        "output": "BASELINE_OUTPUT_PLACEHOLDER",
        "clarity": "variable",
        "drift": "possible"
    }

def main():
    tasks, drift, ambiguity = load_inputs()
    timestamp = datetime.datetime.utcnow().isoformat()

    results = {
        "timestamp": timestamp,
        "tasks": [],
        "drift_tests": [],
        "ambiguity_tests": []
    }

    for t in tasks.splitlines():
        results["tasks"].append(run_baseline_agent(t))

    for d in drift.splitlines():
        results["drift_tests"].append(run_baseline_agent(d))

    for a in ambiguity.splitlines():
        results["ambiguity_tests"].append(run_baseline_agent(a))

    out_dir = Path("benchmark/outputs/sample")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "baseline-summary.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Baseline run complete. Output saved to benchmark/outputs/sample/")

if __name__ == "__main__":
    main()
