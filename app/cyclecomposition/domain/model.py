from dataclasses import dataclass


@dataclass(frozen=True)
class RefName:
    value: str


class Cycle:
    def __init__(self, ref: RefName):
        self.reference: RefName = ref

    def __repr__(self) -> str:
        return f"<Cycle {self.reference}>"

    def __eq__(self, other) -> bool:  # type: ignore
        if not isinstance(other, Cycle):
            return False
        return other.reference == self.reference

    def __hash__(self) -> int:
        return hash(self.reference)
