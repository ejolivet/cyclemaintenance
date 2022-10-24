import json
import os
from typing import Any

import django
from cyclecomposition.service_layer import services, unit_of_work_django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

os.environ["DJANGO_SETTINGS_MODULE"] = "djangoproject.django_project.settings"
django.setup()


@csrf_exempt
def add_cycle(request: Any) -> HttpResponse:
    data = json.loads(request.body)
    services.add_cycle(
        data["ref"],
        unit_of_work_django.DjangoUnitOfWork(),
    )
    return HttpResponse("OK", status=201)
