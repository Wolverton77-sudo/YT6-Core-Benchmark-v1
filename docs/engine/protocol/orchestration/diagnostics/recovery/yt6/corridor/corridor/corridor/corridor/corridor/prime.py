"""
Clarity Prime — Tier‑1

Prime defines the first internal clarity anchor.
It stabilises the system before deeper layers activate.
"""

class ClarityPrime:
    def __init__(self):
        self.anchor = None

    def set_anchor(self, value):
        self.anchor = value

    def describe(self):
        return f"ClarityPrime(anchor={self.anchor})"
