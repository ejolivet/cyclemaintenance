# pylint: disable=no-member
import pytest
from cyclecomposition.domain.model import (
    Component,
    ComponentReference,
    ComponentId,
)
from cyclecomposition.service_layer import unit_of_work_django
from djangoproject.cyclecomp import models as django_models


def insert_cycle(component_id: ComponentId, ref: ComponentReference) -> None:
    django_models.Component.objects.create(
        component_id=component_id.identifier, reference=ref.reference
    )


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_component() -> None:
    uow = unit_of_work_django.DjangoUnitOfWork()

    component_id: ComponentId = uow.components.get_next_id()
    ref = ComponentReference("cycle1", "marque1")

    insert_cycle(component_id, ref)

    cycle = uow.components.get(component_id=component_id)

    assert cycle == Component(component_id, ref)
