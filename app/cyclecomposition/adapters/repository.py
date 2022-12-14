import abc
import uuid
from typing import Set, TypeVar

from ..domain.model import ComponentDTO, ComponentId

T = TypeVar("T", bound="AbstractRepository")


class AbstractRepository(abc.ABC):
    def __init__(self: T) -> None:
        self.seen: Set[ComponentDTO] = set()

    def add(self: T, component: ComponentDTO) -> None:
        self.seen.add(component)

    @staticmethod
    def get_next_id() -> ComponentId:
        component_id: ComponentId = ComponentId.from_uuid(uuid.uuid4())
        return component_id

    def get(self: T, component_id: ComponentId) -> ComponentDTO:
        component: ComponentDTO = self._get(component_id)
        if component:
            self.seen.add(component)
        return component

    @abc.abstractmethod
    def update(self: T, component: ComponentDTO) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self: T, component_id: ComponentId) -> ComponentDTO:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> list[ComponentDTO]:
        raise NotImplementedError
