import json
import os
from typing import Any

import django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from cyclecomposition.domain.commands import CreateComponent
from cyclecomposition.domain.model import ComponentReferenceValue
from cyclecomposition.service_layer import services, unit_of_work_django

os.environ["DJANGO_SETTINGS_MODULE"] = "djangoproject.django_project.settings"
django.setup()


@csrf_exempt
def add_cycle(request: Any) -> HttpResponse:
    data = json.loads(request.body)
    uow = unit_of_work_django.DjangoUnitOfWork()
    command = CreateComponent(
        uow.components.get_next_id(), ComponentReferenceValue(data["ref"])
    )
    services.define_component(
        command=command,
        uow=unit_of_work_django.DjangoUnitOfWork(),
    )
    return HttpResponse("OK", status=201)
