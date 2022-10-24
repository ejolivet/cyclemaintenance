from ..domain.model import Cycle
from ..service_layer import unit_of_work


def add_cycle(
    ref: str,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.cycles.add(Cycle(ref))
        uow.commit()
