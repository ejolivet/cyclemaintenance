from ..domain.model import Cycle, RefValue
from ..service_layer import unit_of_work


def create_cycle(
    ref: RefValue,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.cycles.add(Cycle(ref))
        uow.commit()
