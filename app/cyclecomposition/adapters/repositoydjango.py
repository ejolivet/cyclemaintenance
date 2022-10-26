from djangoproject.cyclecomp import models as django_models

from ..adapters.repository import AbstractRepository
from ..domain.model import Component, ComponentReferenceValue


class DjangoRepository(AbstractRepository):
    def add(self, component: Component) -> None:
        super().add(component)
        self.update(component)

    def update(self, component: Component) -> None:
        django_models.Component.update_from_domain(component)

    def _get(self, reference: ComponentReferenceValue) -> Component:
        return (
            django_models.Component.objects.filter(reference=reference.name)
            .first()
            .to_domain()
        )

    def list(self) -> list[Component]:
        return [b.to_domain() for b in django_models.Component.objects.all()]
