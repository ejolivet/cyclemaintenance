from cyclecomposition.domain.model import Cycle
from cyclecomposition.service_layer import unit_of_work


def add_cycle(
    ref: str,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        uow.cycles.add(Cycle(ref))
        uow.commit()
