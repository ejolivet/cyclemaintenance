from typing import List

from ..domain.commands import Assembly, CreateComponent
from ..domain.model import Component, ComponentDTO
from ..service_layer import unit_of_work


def define_component(
    command: CreateComponent,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.components.add(
            ComponentDTO(
                uid=command.component_id.identifier,
                reference=command.ref.reference,
                marque=command.ref.marque,
            )
        )
        uow.commit()


def get_component_list(
    uow: unit_of_work.AbstractUnitOfWork,
) -> List[ComponentDTO]:
    return uow.components.list()


def mount_component_on(
    command: Assembly,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        child: Component = Component(uow.components.get(command.component_id))
        child.set_parent(command.mout_on_id)
        uow.components.update(child.to_dto())
        uow.commit()
