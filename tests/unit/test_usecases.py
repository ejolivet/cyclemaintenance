from typing import TypeVar, List

from cyclecomposition.domain.commands import CreateComponent, Assembly
from cyclecomposition.domain.model import (
    ComponentId,
    Component,
    ComponentDTO,
    ComponentReference,
)
from cyclecomposition.adapters import repository
from cyclecomposition.service_layer import services, unit_of_work

T = TypeVar("T", bound=repository.AbstractRepository)


class FakeRepository(repository.AbstractRepository):
    """FakeRepository for test"""

    def __init__(self, components: list[Component]) -> None:
        super().__init__()
        self._components = set(components)

    def add(self, component: Component) -> None:
        super().add(component)
        self._components.add(component)

    def _get(self, component_id: ComponentId) -> Component:
        return next(b for b in self._components if b.component_id == component_id)

    def list(self) -> list[ComponentDTO]:
        """getlist of all cycles"""
        return [comp.to_dto() for comp in self._components]

    def update(self: T, component: Component) -> None:
        raise NotImplementedError


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    """FakeUnitOfWork"""

    def __init__(self) -> None:
        super().__init__()
        self.components = FakeRepository([])
        self.committed = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        pass


def test_create_new_component() -> None:
    """test create a new component"""
    uow = FakeUnitOfWork()
    ref = ComponentReference("my_new_cycle", "marque_cycle")
    component_id = uow.components.get_next_id()
    command = CreateComponent(component_id=component_id, ref=ref)
    services.define_component(command, uow)
    assert uow.components.get(component_id) is not None
    assert uow.committed


def test_get_list_of_components_without_parent() -> None:
    uow = FakeUnitOfWork()
    ref_component_1 = ComponentReference("comp_1", "marque_1")
    ref_component_2 = ComponentReference("comp_2", "marque_2")
    id_1 = uow.components.get_next_id()
    command = CreateComponent(component_id=id_1, ref=ref_component_1)
    services.define_component(command, uow)
    id_2 = uow.components.get_next_id()
    command = CreateComponent(component_id=id_2, ref=ref_component_2)
    services.define_component(command, uow)
    expected_component_1: ComponentDTO = ComponentDTO(
        id_1.identifier, ref_component_1.reference, ref_component_1.marque
    )
    expected_component_2: ComponentDTO = ComponentDTO(
        id_2.identifier, ref_component_2.reference, ref_component_2.marque
    )

    components: List[ComponentDTO] = services.get_component_list(uow=uow)

    assert len(uow.components.list()) == 2
    assert set(components) == set([expected_component_1, expected_component_2])


def test_component_mount_on() -> None:
    uow = FakeUnitOfWork()
    ref_component_1 = ComponentReference("comp_1", "marque_1")
    ref_component_2 = ComponentReference("comp_2", "marque_2")
    id_1 = uow.components.get_next_id()
    command = CreateComponent(component_id=id_1, ref=ref_component_1)
    services.define_component(command, uow)
    id_2 = uow.components.get_next_id()
    command = CreateComponent(component_id=id_2, ref=ref_component_2)
    services.define_component(command, uow)

    command_assembly = Assembly(component_id=id_1, mout_on_id=id_2)
    services.mount_component_on(command_assembly, uow)

    assert uow.components.get(id_1).parent_id == id_2
