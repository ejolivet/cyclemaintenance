from cyclecomposition.domain import model as domain_model
from django.db import models


class Cycle(models.Model):
    reference = models.CharField(max_length=255)

    @staticmethod
    def update_from_domain(cycle_domain: domain_model.Cycle) -> None:
        try:
            cycle = Cycle.objects.get(reference=cycle_domain.reference)
        except Cycle.DoesNotExist:
            cycle = Cycle(reference=cycle_domain.reference)
        cycle.save()

    # noinspection PyTypeChecker
    def to_domain(self) -> domain_model.Cycle:
        cycle_domain = domain_model.Cycle(ref=self.reference)
        return cycle_domain
