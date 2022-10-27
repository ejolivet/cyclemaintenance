from dataclasses import dataclass

from .model import ComponentId, ComponentReference


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class CreateComponent(Command):
    component_id: ComponentId
    ref: ComponentReference
