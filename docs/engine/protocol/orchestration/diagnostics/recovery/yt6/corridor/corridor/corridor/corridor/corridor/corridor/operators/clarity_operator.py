"""
Clarity Operator — Tier‑2

This operator enforces clarity rules on incoming data.
It is used by the core engine and benchmark tasks.
"""

class ClarityOperator:
    def __init__(self):
        self.last_input = None
        self.last_output = None

    def apply(self, data):
        self.last_input = data
        clarified = f"clarity({data})"
        self.last_output = clarified
        return clarified

    def state(self):
        return {
            "last_input": self.last_input,
            "last_output": self.last_output
        }
