# pylint: disable=no-member
import pytest
from cyclecomposition.domain.model import (
    Component,
    ComponentReferenceValue,
    ComponentId,
)
from cyclecomposition.service_layer import unit_of_work_django
from djangoproject.cyclecomp import models as django_models


def insert_cycle(component_id: ComponentId, ref: ComponentReferenceValue) -> None:
    django_models.Component.objects.create(
        component_id=component_id.identifier, reference=ref.name
    )


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_cycle() -> None:
    uow = unit_of_work_django.DjangoUnitOfWork()

    component_id: ComponentId = uow.components.get_next_id()
    ref = ComponentReferenceValue("cycle1")

    insert_cycle(component_id, ref)

    cycle = uow.components.get(component_id=component_id)

    assert cycle == Component(component_id, ref)
