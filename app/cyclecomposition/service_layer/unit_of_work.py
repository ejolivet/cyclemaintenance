import abc
from typing import Any, TypeVar

from ..adapters import repository

T = TypeVar("T", bound="AbstractUnitOfWork")


class AbstractUnitOfWork(abc.ABC):
    cycles: repository.AbstractRepository

    def __init__(self: T) -> None:
        pass

    def __enter__(self: T) -> T:
        return self

    def __exit__(self: T, *args: tuple[Any, ...]) -> None:
        self.rollback()

    @abc.abstractmethod
    def commit(self: T) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self: T) -> None:
        raise NotImplementedError
