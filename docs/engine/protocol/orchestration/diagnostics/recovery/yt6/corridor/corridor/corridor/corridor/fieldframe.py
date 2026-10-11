"""
Clarity Fieldframe — Tier‑1

The Fieldframe binds the Clarity Field and Clarity Frame together.
It defines how external clarity (Field) interacts with structural clarity (Frame).
"""

class ClarityFieldframe:
    def __init__(self, field, frame):
        self.field = field
        self.frame = frame

    def bind(self):
        return {
            "field": self.field.describe(),
            "frame": self.frame.view()
        }

    def summary(self):
        return f"Fieldframe(bound: field={self.field.environment}, frame={self.frame.boundaries})"
