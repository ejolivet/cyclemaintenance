from dataclasses import dataclass, field
from uuid import UUID


@dataclass(frozen=True)
class ComponentReference:
    reference: str
    marque: str


@dataclass(frozen=True)
class ComponentId:
    identifier: str

    @classmethod
    def from_uuid(cls, uuid: UUID) -> "ComponentId":
        return ComponentId(str(uuid))


@dataclass(frozen=True, order=True)
class ComponentDTO:
    sort_index: str = field(init=False, repr=False)

    uid: str
    reference: str
    marque: str
    mounted_on: str = "none"

    def __post_init__(self) -> None:
        # sort by uid
        object.__setattr__(self, "sort_index", self.uid)


class Component:
    def __init__(
        self,
        component_dto: ComponentDTO,
    ) -> None:
        self.component_id: ComponentId = ComponentId(component_dto.uid)
        self.reference: ComponentReference = ComponentReference(
            component_dto.reference, component_dto.marque
        )
        self.parent_id: ComponentId = ComponentId(component_dto.mounted_on)

    def to_dto(self) -> ComponentDTO:
        return ComponentDTO(
            uid=self.component_id.identifier,
            reference=self.reference.reference,
            marque=self.reference.marque,
            mounted_on=self.parent_id.identifier,
        )

    def set_parent(self, parent_id: ComponentId) -> None:
        self.parent_id = parent_id

    def __repr__(self) -> str:
        return f"<Cycle {self.component_id.identifier} - {self.reference.reference}>"

    def __eq__(self, other) -> bool:  # type: ignore
        if not isinstance(other, Component):
            return False
        return other.component_id == self.component_id

    def __hash__(self) -> int:
        return hash(self.component_id)
