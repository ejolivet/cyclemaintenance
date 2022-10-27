from dataclasses import dataclass

from .model import ComponentId, ComponentReferenceValue


class Command:
    pass


@dataclass
class CreateComponent(Command):
    id: ComponentId
    ref: ComponentReferenceValue
