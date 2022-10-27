from dataclasses import dataclass


@dataclass(frozen=True)
class ComponentReference:
    reference: str
    marque: str


@dataclass(frozen=True)
class ComponentId:
    identifier: str

    @classmethod
    def from_string(cls, string_id: str) -> "ComponentId":
        return ComponentId(string_id)


class Component:
    def __init__(self, component_id: ComponentId, ref: ComponentReference):
        self.component_id: ComponentId = component_id
        self.reference: ComponentReference = ref

    def __repr__(self) -> str:
        return f"<Cycle {self.component_id.identifier} - {self.reference.reference}>"

    def __eq__(self, other) -> bool:  # type: ignore
        if not isinstance(other, Component):
            return False
        return other.component_id == self.component_id

    def __hash__(self) -> int:
        return hash(self.component_id)
