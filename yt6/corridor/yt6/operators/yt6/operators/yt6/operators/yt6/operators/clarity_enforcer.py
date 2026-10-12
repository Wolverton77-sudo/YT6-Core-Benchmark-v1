"""
YT6 Operators — Clarity Enforcer Operator

Purpose:
- Enforce clarity invariants
- Ensure responses remain aligned with the corridor
- Provide deterministic clarity decisions
"""

from dataclasses import dataclass
from typing import Dict, Any

from yt6.corridor.primeframe import Primeframe
from .drift_resistant import DriftResistantOperator, DriftAssessment


@dataclass
class ClarityDecision:
    clarity_ok: bool
    reason: str
    details: Dict[str, Any]


class ClarityEnforcer:
    """
    ClarityEnforcer:
    Applies clarity rules on top of drift assessment.
    """

    def __init__(self):
        self.drift_operator = DriftResistantOperator()

    def enforce(self, primeframe: Primeframe) -> ClarityDecision:
        drift: DriftAssessment = self.drift_operator.evaluate(primeframe)

        if drift.drift_detected:
            return ClarityDecision(
                clarity_ok=False,
                reason=f"DRIFT: {drift.reason}",
                details=drift.details,
            )

        signals = primeframe.signals_dict()

        if signals["turn_count"] == 0:
            return ClarityDecision(
                clarity_ok=False,
                reason="EMPTY_SESSION",
                details=signals,
            )

        # Basic clarity invariant: both sides must contribute
        if not signals["has_user_input"] or not signals["has_system_output"]:
            return ClarityDecision(
                clarity_ok=False,
                reason="MISSING_PARTICIPATION",
                details=signals,
            )

        return ClarityDecision(
            clarity_ok=True,
            reason="CLEAR",
            details=signals,
        )
