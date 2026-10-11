"""
Stability Operator — Tier‑2

This operator enforces stability and drift‑resistance.
It ensures the system behaves consistently across turns.
"""

class StabilityOperator:
    def __init__(self):
        self.stability_score = 1.0  # starts fully stable

    def reinforce(self):
        """Increase stability slightly."""
        self.stability_score = min(1.0, self.stability_score + 0.01)
        return self.stability_score

    def weaken(self):
        """Decrease stability slightly."""
        self.stability_score = max(0.0, self.stability_score - 0.01)
        return self.stability_score

    def status(self):
        return f"Stability(score={self.stability_score})"
