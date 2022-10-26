from django.db import models

from cyclecomposition.domain import model as domain_model


class Component(models.Model):
    reference = models.CharField(max_length=255)

    @staticmethod
    def update_from_domain(component_domain: domain_model.Component) -> None:
        try:
            component = Component.objects.get(reference=component_domain.reference.name)
        except Component.DoesNotExist:
            component = Component(reference=component_domain.reference.name)
        component.save()

    # noinspection PyTypeChecker
    def to_domain(self) -> domain_model.Component:
        component_domain = domain_model.Component(
            ref=domain_model.ComponentReferenceValue(self.reference)
        )
        return component_domain
