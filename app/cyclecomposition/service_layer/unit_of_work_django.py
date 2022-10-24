from typing import Any, TypeVar

from cyclecomposition.adapters.repositoydjango import DjangoRepository
from cyclecomposition.service_layer.unit_of_work import AbstractUnitOfWork
from django.db import transaction

T = TypeVar("T", bound="DjangoUnitOfWork")


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self: T) -> None:
        self.cycles: DjangoRepository = DjangoRepository()

    def __enter__(self: T) -> T:
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
