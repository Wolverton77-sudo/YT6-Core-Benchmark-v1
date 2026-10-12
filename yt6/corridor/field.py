"""
YT6 Clarity Corridor — Field layer

The Field is the lowest layer of the corridor.
It holds raw interaction context: user input, system output, and environment signals.
It is responsible for:
- capturing state without interpretation
- preserving a deterministic record of each turn
- providing a stable substrate for higher layers (Frame, Fieldframe, Prime, Primeframe)
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class TurnRecord:
    turn_id: int
    user_input: str
    system_output: str
    metadata: Dict[str, Any]


@dataclass
class Field:
    """
    Field: raw interaction substrate.

    This class is intentionally simple and deterministic:
    - no hidden mutation
    - all state is explicit
    - every turn is recorded as a TurnRecord
    """

    turns: List[TurnRecord] = field(default_factory=list)

    def add_turn(
        self,
        turn_id: int,
        user_input: str,
        system_output: str,
        metadata: Dict[str, Any] | None = None,
    ) -> None:
        if metadata is None:
            metadata = {}

        record = TurnRecord(
            turn_id=turn_id,
            user_input=user_input,
            system_output=system_output,
            metadata=metadata,
        )
        self.turns.append(record)

    def get_turn(self, turn_id: int) -> TurnRecord | None:
        for t in self.turns:
            if t.turn_id == turn_id:
                return t
        return None

    def all_turns(self) -> List[TurnRecord]:
        return list(self.turns)

    def size(self) -> int:
        return len(self.turns)
