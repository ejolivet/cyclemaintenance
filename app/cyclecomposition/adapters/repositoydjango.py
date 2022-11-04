from djangoproject.cyclecomp import models as django_models

from ..adapters.repository import AbstractRepository
from ..domain.model import Component, ComponentDTO, ComponentId


class DjangoRepository(AbstractRepository):
    def add(self, component: Component) -> None:
        super().add(component)
        self.update(component)

    def update(self, component: Component) -> None:
        django_models.Component.update_from_domain(component)

    def _get(self, component_id: ComponentId) -> Component:
        return (
            django_models.Component.objects.filter(component_id=component_id.identifier)
            .first()
            .to_domain()
        )

    def list(self) -> list[ComponentDTO]:
        return [b.to_domain().to_dto() for b in django_models.Component.objects.all()]
