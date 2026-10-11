"""
Clarity Primeframe — Tier‑1

Primeframe binds Prime to the Fieldframe.
It creates the first stable clarity structure inside the corridor.
"""

class ClarityPrimeframe:
    def __init__(self, prime, fieldframe):
        self.prime = prime
        self.fieldframe = fieldframe

    def bind(self):
        return {
            "prime": self.prime.describe(),
            "fieldframe": self.fieldframe.summary()
        }

    def summary(self):
        return f"Primeframe(prime={self.prime.anchor}, fieldframe={self.fieldframe.bind()})"
