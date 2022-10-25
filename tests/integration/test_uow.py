# pylint: disable=no-member
import pytest
from cyclecomposition.domain.model import Cycle, RefValue
from cyclecomposition.service_layer import unit_of_work_django
from djangoproject.cyclecomp import models as django_models


def insert_cycle(ref: RefValue) -> None:
    django_models.Cycle.objects.create(reference=ref.value)


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_cycle() -> None:
    ref = RefValue("cycle1")
    insert_cycle(ref)

    uow = unit_of_work_django.DjangoUnitOfWork()
    cycle = uow.cycles.get(reference=ref)

    assert cycle == Cycle(ref)
