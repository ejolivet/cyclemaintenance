from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T", bound="ComponentId")


@dataclass(frozen=True)
class ComponentReferenceValue:
    name: str


@dataclass(frozen=True)
class ComponentId:
    id: str

    @classmethod
    def from_string(cls, string_id: str) -> T:
        return ComponentId(string_id)


class Component:
    def __init__(self, component_id: ComponentId, ref: ComponentReferenceValue):
        self.id: ComponentId = component_id
        self.reference: ComponentReferenceValue = ref

    def __repr__(self) -> str:
        return f"<Cycle {self.reference}>"

    def __eq__(self, other) -> bool:  # type: ignore
        if not isinstance(other, Component):
            return False
        return other.reference == self.reference

    def __hash__(self) -> int:
        return hash(self.reference)
