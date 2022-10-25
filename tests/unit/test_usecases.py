from typing import TypeVar

from cyclecomposition.domain.model import Cycle, RefName
from cyclecomposition.adapters import repository
from cyclecomposition.service_layer import services, unit_of_work

T = TypeVar("T", bound=repository.AbstractRepository)


class FakeRepository(repository.AbstractRepository):
    """FakeRepository for test"""

    def __init__(self, cycles: list[Cycle]) -> None:
        super().__init__()
        self._cycles = set(cycles)
        super().__init__()

    def add(self, cycle: Cycle) -> None:
        super().add(cycle)
        self._cycles.add(cycle)
        super().add(cycle)

    def _get(self, reference: RefName) -> Cycle:
        return next(b for b in self._cycles if b.reference == reference)

    def list(self) -> list[Cycle]:
        """getlist of all cycles"""
        return list(self._cycles)

    def update(self: T, cycle: Cycle) -> None:
        raise NotImplementedError


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    """FakeUnitOfWork"""

    def __init__(self) -> None:
        super().__init__()
        self.cycles = FakeRepository([])
        self.committed = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        pass


def test_create_new_cycle() -> None:
    """test create a new cycle"""
    uow = FakeUnitOfWork()
    ref = RefName("my_new_cycle")
    services.add_cycle(ref, uow)
    assert uow.cycles.get(ref) is not None
    assert uow.committed
