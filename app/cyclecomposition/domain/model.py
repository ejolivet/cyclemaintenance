from dataclasses import dataclass


@dataclass(frozen=True)
class ComponentReferenceValue:
    name: str


class Component:
    def __init__(self, ref: ComponentReferenceValue):
        self.reference: ComponentReferenceValue = ref

    def __repr__(self) -> str:
        return f"<Cycle {self.reference}>"

    def __eq__(self, other) -> bool:  # type: ignore
        if not isinstance(other, Component):
            return False
        return other.reference == self.reference

    def __hash__(self) -> int:
        return hash(self.reference)
