from typing import TypeVar, Any

from django.db import transaction

from ..adapters.repositoydjango import DjangoRepository
from .unit_of_work import AbstractUnitOfWork

T = TypeVar("T", bound="DjangoUnitOfWork")


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __enter__(self: T) -> T:
        self.cycles: DjangoRepository = DjangoRepository()
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self: T, *args: tuple[Any, ...]) -> None:
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self: T) -> None:
        for cycle in self.cycles.seen:
            self.cycles.update(cycle)
        transaction.commit()

    def rollback(self: T) -> None:
        transaction.rollback()
