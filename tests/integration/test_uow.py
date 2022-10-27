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

    component_id = uow.components.get_next_id()
    ref = ComponentReference("cycle1", "marque1")

    insert_cycle(component_id, ref)

    component = uow.components.get(component_id=component_id)

    assert component == Component(component_id, ref)


@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_an_assembly() -> None:
    uow = unit_of_work_django.DjangoUnitOfWork()

    id_1 = uow.components.get_next_id()
    ref_1 = ComponentReference("comp_1", "marque_1")
    id_2 = uow.components.get_next_id()
    ref_2 = ComponentReference("comp_2", "marque_2")

    insert_cycle(id_1, ref_1)
    insert_cycle(id_2, ref_2)

    comp_1 = uow.components.get(component_id=id_1)
    comp_1.set_parent(id_2)
    uow.components.update(comp_1)

    assert uow.components.get(component_id=id_1).parent_id == id_2
