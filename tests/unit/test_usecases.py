from typing import TypeVar

from cyclecomposition.domain.model import Component, ComponentReferenceValue
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

    def _get(self, reference: ComponentReferenceValue) -> Component:
        return next(b for b in self._components if b.reference == reference)

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


def test_create_new_cycle() -> None:
    """test create a new cycle"""
    uow = FakeUnitOfWork()
    ref = ComponentReferenceValue("my_new_cycle")
    services.define_component(ref, uow)
    assert uow.components.get(ref) is not None
    assert uow.committed
