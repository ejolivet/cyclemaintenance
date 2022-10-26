from ..domain.model import Component, ComponentReferenceValue
from ..service_layer import unit_of_work


def define_component(
    ref: ComponentReferenceValue,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.components.add(Component(ref))
        uow.commit()
