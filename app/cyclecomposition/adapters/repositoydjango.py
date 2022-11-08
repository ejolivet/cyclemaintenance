from djangoproject.cyclecomp import models as django_models

from ..adapters.repository import AbstractRepository
from ..domain.model import ComponentDTO, ComponentId


class DjangoRepository(AbstractRepository):
    def add(self, component: ComponentDTO) -> None:
        super().add(component)
        self.update(component)

    def update(self, component: ComponentDTO) -> None:
        django_models.Component.update_from_dto(component)

    def _get(self, component_id: ComponentId) -> ComponentDTO:
        return (
            django_models.Component.objects.filter(component_id=component_id.identifier)
            .first()
            .to_dto()
        )

    def list(self) -> list[ComponentDTO]:
        return [b.to_dto() for b in django_models.Component.objects.all()]
