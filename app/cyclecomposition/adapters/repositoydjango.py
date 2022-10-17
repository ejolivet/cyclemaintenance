from djangoproject.cyclecomposition import models as django_models

from ..domain.model import Cycle
from ..adapters.repository import AbstractRepository


class DjangoRepository(AbstractRepository):
    def add(self, cycle: Cycle) -> None:
        super().add(cycle)
        self.update(cycle)

    def update(self, cycle: Cycle) -> None:
        django_models.Cycle.update_from_domain(cycle)

    def _get(self, reference: str) -> Cycle:
        return (
            django_models.Cycle.objects.filter(reference=reference).first().to_domain()
        )

    def list(self) -> list[Cycle]:
        return [b.to_domain() for b in django_models.Cycle.objects.all()]
