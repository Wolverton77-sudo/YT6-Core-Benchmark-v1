"""
YT6 Operators — Deterministic operator

Ensures the system behaves predictably:
- no hidden state
- no random behaviour
- all decisions traceable to inputs
"""

from dataclasses import dataclass
from typing import Any, Dict

from yt6.corridor.primeframe import Primeframe


@dataclass
class DeterministicOperatorResult:
    decision: str
    details: Dict[str, Any]


class DeterministicOperator:
    """
    DeterministicOperator:
    Given a Primeframe, produce a deterministic decision
    about whether the interaction is in a valid, stable state.
    """

    def evaluate(self, primeframe: Primeframe) -> DeterministicOperatorResult:
        signals = primeframe.signals_dict()

        if signals["turn_count"] == 0:
            decision = "EMPTY_SESSION"
        elif not signals["has_user_input
