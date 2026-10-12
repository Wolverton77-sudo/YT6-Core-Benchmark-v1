"""
YT6 Operators — Drift Resistant Operator

Purpose:
- Detect conversational drift using Primeframe signals
- Apply containment logic
- Produce a deterministic drift assessment
"""

from dataclasses import dataclass
from typing import Dict, Any

from yt6.corridor.primeframe import Primeframe


@dataclass
class DriftAssessment:
    drift_detected: bool
    drift_score: float
    reason: str
    details: Dict[str, Any]


class DriftResistantOperator:
    """
    DriftResistantOperator:
    Evaluates whether the interaction is drifting away from clarity.
    """

    def evaluate(self, primeframe: Primeframe) -> DriftAssessment:
        signals = primeframe.signals_dict()

        turn_count = signals["turn_count"]
        last_user = signals["last_user_input"]
        last_system = signals["last_system_output"]

        # Simple drift heuristic: empty or mismatched turns
        if turn_count == 0:
            return DriftAssessment(
                drift_detected=False,
                drift_score=0.0,
                reason="EMPTY_SESSION",
                details=signals,
            )

        if last_user is None:
            return DriftAssessment(
                drift_detected=True,
                drift_score=0.7,
                reason="NO_USER_INPUT",
                details=signals,
            )

        if last_system is None:
            return DriftAssessment(
                drift_detected=True,
                drift_score=0.6,
                reason="NO_SYSTEM_OUTPUT",
                details=signals,
            )

        # Basic clarity mismatch detection
        if len(last_user) > 0 and len(last_system) == 0:
            return DriftAssessment(
                drift_detected=True,
                drift_score=0.5,
                reason="SYSTEM_NOT_RESPONDING",
                details=signals,
            )

        # No drift detected
        return DriftAssessment(
            drift_detected=False,
            drift_score=0.0,
            reason="STABLE",
            details=signals,
        )
