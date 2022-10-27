from django.db import models

from cyclecomposition.domain import model as domain_model


class Component(models.Model):
    component_id = models.CharField(max_length=16, primary_key=True)
    reference = models.CharField(max_length=255)

    @staticmethod
    def update_from_domain(component_domain: domain_model.Component) -> None:
        try:
            component = Component.objects.get(
                component_id=component_domain.component_id.identifier
            )
        except Component.DoesNotExist:
            component = Component(
                component_id=component_domain.component_id.identifier,
                reference=component_domain.reference.name,
            )
        component.save()

    # noinspection PyTypeChecker
    def to_domain(self) -> domain_model.Component:
        component_domain = domain_model.Component(
            component_id=domain_model.ComponentId.from_string(self.component_id),
            ref=domain_model.ComponentReferenceValue(self.reference),
        )
        return component_domain
