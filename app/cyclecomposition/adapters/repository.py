import abc
from typing import Set, TypeVar

from ..domain.model import Cycle, RefValue

T = TypeVar("T", bound="AbstractRepository")


class AbstractRepository(abc.ABC):
    def __init__(self: T) -> None:
        self.seen: Set[Cycle] = set()

    def add(self: T, cycle: Cycle) -> None:
        self.seen.add(cycle)

    def get(self: T, reference: RefValue) -> Cycle:
        cycle: Cycle = self._get(reference)
        if cycle:
            self.seen.add(cycle)
        return cycle

    @abc.abstractmethod
    def update(self: T, cycle: Cycle) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self: T, reference: RefValue) -> Cycle:
        raise NotImplementedError
