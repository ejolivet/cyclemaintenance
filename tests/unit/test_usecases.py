from typing import TypeVar

from cyclecomposition.domain.commands import CreateComponent
from cyclecomposition.domain.model import (
    ComponentId,
    Component,
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

    def list(self) -> list[Component]:
        """getlist of all cycles"""
        return list(self._components)

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
    """test create a new cycle"""
    uow = FakeUnitOfWork()
    ref = ComponentReference("my_new_cycle", "marque_cycle")
    component_id = uow.components.get_next_id()
    command = CreateComponent(component_id=component_id, ref=ref)
    services.define_component(command, uow)
    assert uow.components.get(component_id) is not None
    assert uow.committed
