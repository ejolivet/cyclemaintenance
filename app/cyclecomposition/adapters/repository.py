import abc
from typing import Set, TypeVar

from cyclecomposition.domain.model import Cycle

T = TypeVar("T", bound="AbstractRepository")


class AbstractRepository(abc.ABC):
    def __init__(self: T) -> None:
        self.seen: Set[Cycle] = set()

    def add(self: T, cycle: Cycle) -> None:
        self.seen.add(cycle)

    def get(self: T, reference: str) -> Cycle:
        cycle: Cycle = self._get(reference)
        if cycle:
            self.seen.add(cycle)
        return cycle

    @abc.abstractmethod
    def update(self: T, cycle: Cycle) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self: T, reference: str) -> Cycle:
        raise NotImplementedError
