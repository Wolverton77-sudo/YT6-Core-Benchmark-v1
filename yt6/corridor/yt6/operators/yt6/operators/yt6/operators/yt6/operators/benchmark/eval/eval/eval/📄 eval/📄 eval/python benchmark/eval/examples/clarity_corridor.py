"""
YT6 Example — Clarity Corridor Demonstration

Shows how Field, Frame, Fieldframe, Prime, and Primeframe
work together in a real interaction.
"""

from yt6.corridor.field import Field
from yt6.corridor.frame import Frame
from yt6.corridor.fieldframe import Fieldframe
from yt6.corridor.primeframe import Primeframe


def demo():
    field = Field()
    frame = Frame(field=field, episode_id="example_01")
    ff = Fieldframe(field=field, frame=frame)

    ff.add_turn(
        turn_id=1,
        user_input="Hello",
        system_output="Hi, how can I help?",
        metadata={"example": True},
    )

    pf = Primeframe.from_fieldframe(ff)

    print("=== Clarity Corridor Example ===")
    print("Episode:", pf.episode_id())
    print("Length:", pf.length())
    print("Signals:", pf.signals_dict())


if __name__ == "__main__":
    demo()
