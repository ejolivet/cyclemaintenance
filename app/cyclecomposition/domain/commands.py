from dataclasses import dataclass

from .model import ComponentId, ComponentReferenceValue


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class CreateComponent(Command):
    component_id: ComponentId
    ref: ComponentReferenceValue
