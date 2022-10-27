from ..domain.commands import CreateComponent
from ..domain.model import Component, ComponentReferenceValue
from ..service_layer import unit_of_work


def define_component(
    command: CreateComponent,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.components.add(Component(component_id=command.id, ref=command.ref))
        uow.commit()
