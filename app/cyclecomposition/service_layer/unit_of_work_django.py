from typing import Any, TypeVar

from django.db import transaction

from ..adapters.repositoydjango import DjangoRepository
from ..service_layer.unit_of_work import AbstractUnitOfWork

T = TypeVar("T", bound="DjangoUnitOfWork")


class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self: T) -> None:
        super().__init__()
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
