import abc
from typing import Set, TypeVar

from ..domain.model import Component, ComponentReferenceValue

T = TypeVar("T", bound="AbstractRepository")


class AbstractRepository(abc.ABC):
    def __init__(self: T) -> None:
        self.seen: Set[Component] = set()

    def add(self: T, component: Component) -> None:
        self.seen.add(component)

    def get(self: T, reference: ComponentReferenceValue) -> Component:
        component: Component = self._get(reference)
        if component:
            self.seen.add(component)
        return component

    @abc.abstractmethod
    def update(self: T, component: Component) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self: T, reference: ComponentReferenceValue) -> Component:
        raise NotImplementedError
