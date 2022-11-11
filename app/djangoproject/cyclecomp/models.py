from django.db import models

from cyclecomposition.domain import model as domain_model


class Component(models.Model):
    component_id = models.CharField(max_length=16, primary_key=True)
    reference = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    parent = models.CharField(max_length=16, default="none")

    @staticmethod
    def update_from_domain(component_domain: domain_model.Component) -> None:
        try:
            component = Component.objects.get(
                component_id=component_domain.component_id.identifier
            )
            component.reference = component_domain.reference.reference
            component.marque = component_domain.reference.marque
        except Component.DoesNotExist:
            component = Component(
                component_id=component_domain.component_id.identifier,
                reference=component_domain.reference.reference,
                marque=component_domain.reference.marque,
            )
        component.parent = component_domain.parent_id.identifier
        component.save()

    # noinspection PyTypeChecker
    def to_domain(self) -> domain_model.Component:
        parent = "none"
        if self.parent:
            parent = self.parent
        component_dto: domain_model.ComponentDTO = domain_model.ComponentDTO(
            uid=self.component_id,
            reference=self.reference,
            marque=self.marque,
            mounted_on=parent,
        )
        component = domain_model.Component(component_dto)
        return component
