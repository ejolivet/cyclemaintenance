from dataclasses import dataclass

from .model import ComponentId, ComponentReference


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class CreateComponent(Command):
    component_id: ComponentId
    ref: ComponentReference


@dataclass(frozen=True)
class Assembly(Command):
    component_id: ComponentId
    mout_on_id: ComponentId
