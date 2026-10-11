"""
Clarity Field — Tier‑1

The Clarity Field defines the external clarity environment.
"""

class ClarityField:
    def __init__(self):
        self.environment = {}

    def set(self, key, value):
        self.environment[key] = value

    def get(self, key):
        return self.environment.get(key, None)

    def describe(self):
        return f"ClarityField: {self.environment}"
