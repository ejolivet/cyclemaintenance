# pylint: disable=no-member
import pytest
from cyclecomposition.domain.model import Cycle
from cyclecomposition.service_layer import unit_of_work_django
from djangoproject.cyclecomp import models as django_models


def insert_cycle(ref: str) -> None:
    django_models.Cycle.objects.create(reference=ref)


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_cycle() -> None:
    insert_cycle("cycle1")

    uow = unit_of_work_django.DjangoUnitOfWork()
    cycle = uow.cycles.get(reference="cycle1")

    assert cycle == Cycle("cycle1")
