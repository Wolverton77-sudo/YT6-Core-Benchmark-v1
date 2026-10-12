"""
YT6 Benchmark Runner

Executes all benchmark tasks using:
- Field
- Frame
- Fieldframe
- Prime
- Primeframe
- DeterministicOperator
- DriftResistantOperator
- ClarityEnforcer

Produces:
- logs
- traces
- snapshot.md
"""

import os
import json
from datetime import datetime

from yt6.corridor.field import Field
from yt6.corridor.frame import Frame
from yt6.corridor.fieldframe import Fieldframe
from yt6.corridor.primeframe import Primeframe

from yt6.operators.deterministic import DeterministicOperator
from yt6.operators.drift_resistant import DriftResistantOperator
from yt6.operators.clarity_enforcer import ClarityEnforcer


class BenchmarkRunner:
    def __init__(self):
        self.det = DeterministicOperator()
        self.drift = DriftResistantOperator()
        self.clarity = ClarityEnforcer()

    def run_task(self, task_id: int, user_input: str, system_output: str):
        field = Field()
        frame = Frame(field=field, episode_id=f"task_{task_id}")
        ff = Fieldframe(field=field, frame=frame)

        ff.add_turn(
            turn_id=1,
            user_input=user_input,
            system_output=system_output,
            metadata={"task_id": task_id},
        )

        pf = Primeframe.from_fieldframe(ff)

        det = self.det.evaluate(pf)
        drift = self.drift.evaluate(pf)
        clarity = self.clarity.enforce(pf)

        return {
            "task_id": task_id,
            "signals": pf.signals_dict(),
            "deterministic": det.details,
            "drift": {
                "detected": drift.drift_detected,
                "score": drift.drift_score,
                "reason": drift.reason,
            },
            "clarity": {
                "ok": clarity.clarity_ok,
                "reason": clarity.reason,
            },
        }

    def run_all(self):
        results = []
        for i in range(1, 21):
            task_file = f"benchmark/tasks/task_{i:02d}.md"
            with open(task_file, "r") as f:
                content = f.read().strip().split("\n")
                user_input = content[1].replace("USER: ", "")
                system_output = content[2].replace("SYSTEM: ", "")

            result = self.run_task(i, user_input, system_output)
            results.append(result)

        timestamp = datetime.utcnow().isoformat()
        snapshot_path = "benchmark/results/snapshot.md"

        with open(snapshot_path, "w") as f:
            f.write(f"# Benchmark Snapshot — {timestamp}\n\n")
            f.write(json.dumps(results, indent=4))

        return results


if __name__ == "__main__":
    runner = BenchmarkRunner()
    runner.run_all()
