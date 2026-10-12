"""
YT6 Example — Multi-Turn Interaction Demo

Demonstrates:
- multiple turns
- drift detection
- clarity enforcement
"""

from yt6.corridor.field import Field
from yt6.corridor.frame import Frame
from yt6.corridor.fieldframe import Fieldframe
from yt6.corridor.primeframe import Primeframe

from yt6.operators.deterministic import DeterministicOperator
from yt6.operators.drift_resistant import DriftResistantOperator
from yt6.operators.clarity_enforcer import ClarityEnforcer


def demo():
    field = Field()
    frame = Frame(field=field, episode_id="multi_turn_demo")
    ff = Fieldframe(field=field, frame=frame)

    turns = [
        ("Hello", "Hi there!"),
        ("Can you help me?", "Of course."),
        ("", "I'm still here."),
    ]

    for i, (user, system) in enumerate(turns, start=1):
        ff.add_turn(turn_id=i, user_input=user, system_output=system)

    pf = Primeframe.from_fieldframe(ff)

    det = DeterministicOperator().evaluate(pf)
    drift = DriftResistantOperator().evaluate(pf)
    clarity = ClarityEnforcer().enforce(pf)

    print("=== Multi-Turn Demo ===")
    print("Signals:", pf.signals_dict())
    print("Deterministic:", det.details)
    print("Drift:", drift.reason, drift.drift_score)
    print("Clarity:", clarity.reason)


if __name__ == "__main__":
    demo()
