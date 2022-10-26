# pylint: disable=no-member
import pytest
from cyclecomposition.domain.model import Component, ComponentReferenceValue
from cyclecomposition.service_layer import unit_of_work_django
from djangoproject.cyclecomp import models as django_models


def insert_cycle(ref: ComponentReferenceValue) -> None:
    django_models.Component.objects.create(reference=ref.name)


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_cycle() -> None:
    ref = ComponentReferenceValue("cycle1")
    insert_cycle(ref)

    uow = unit_of_work_django.DjangoUnitOfWork()
    cycle = uow.components.get(reference=ref)

    assert cycle == Component(ref)
