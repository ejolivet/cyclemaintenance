from django.db import models

from cyclecomposition.domain.model import ComponentDTO


class Component(models.Model):
    component_id = models.CharField(max_length=16, primary_key=True)
    reference = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    parent = models.CharField(max_length=16, default="none")

    @staticmethod
    def update_from_dto(component_dto: ComponentDTO) -> None:
        try:
            component = Component.objects.get(component_id=component_dto.uid)
            component.reference = component_dto.reference
            component.marque = component_dto.marque
        except Component.DoesNotExist:
            component = Component(
                component_id=component_dto.uid,
                reference=component_dto.reference,
                marque=component_dto.marque,
            )
        component.parent = component_dto.mounted_on
        component.save()

    # noinspection PyTypeChecker
    def to_dto(self) -> ComponentDTO:
        component_dto = ComponentDTO(
            uid=self.component_id,
            reference=self.reference,
            marque=self.marque,
            mounted_on=self.parent,
        )
        return component_dto
