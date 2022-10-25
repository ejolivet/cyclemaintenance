from djangoproject.cyclecomp import models as django_models

from ..adapters.repository import AbstractRepository
from ..domain.model import Cycle, RefValue


class DjangoRepository(AbstractRepository):
    def add(self, cycle: Cycle) -> None:
        super().add(cycle)
        self.update(cycle)

    def update(self, cycle: Cycle) -> None:
        django_models.Cycle.update_from_domain(cycle)

    def _get(self, reference: RefValue) -> Cycle:
        return (
            django_models.Cycle.objects.filter(reference=reference.value)
            .first()
            .to_domain()
        )

    def list(self) -> list[Cycle]:
        return [b.to_domain() for b in django_models.Cycle.objects.all()]
