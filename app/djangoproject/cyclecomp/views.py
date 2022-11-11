import os
from typing import Any, List

import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cyclecomposition.domain.commands import CreateComponent
from cyclecomposition.domain.model import ComponentDTO, ComponentId, ComponentReference
from cyclecomposition.service_layer import services, unit_of_work_django

os.environ["DJANGO_SETTINGS_MODULE"] = "djangoproject.django_project.settings"
django.setup()


def define_component(request: Any) -> HttpResponse:
    uow = unit_of_work_django.DjangoUnitOfWork()
    command = CreateComponent(
        uow.components.get_next_id(),
        ComponentReference(
            reference=request.POST["reference"], marque=request.POST["marque"]
        ),
    )
    services.define_component(
        command=command,
        uow=uow,
    )
    return HttpResponseRedirect("/cyclecomp/")


@csrf_exempt
def define_component_api(request: Any) -> HttpResponse:
    uow = unit_of_work_django.DjangoUnitOfWork()
    command = CreateComponent(
        uow.components.get_next_id(),
        ComponentReference(
            reference=request.POST["reference"], marque=request.POST["marque"]
        ),
    )
    services.define_component(
        command=command,
        uow=uow,
    )
    return HttpResponse("OK", status=201)


def detail(request: Any, component_id: str) -> HttpResponse:
    uow = unit_of_work_django.DjangoUnitOfWork()
    component_dto: ComponentDTO = uow.components.get(ComponentId(component_id)).to_dto()
    return render(request, "cyclecomp/detail.html", {"cyclecomp": component_dto})


def index(request: Any) -> HttpResponse:
    uow = unit_of_work_django.DjangoUnitOfWork()
    component_list: List[ComponentDTO] = services.get_component_list(uow)
    context = {"component_list": component_list}
    return render(request, "cyclecomp/index.html", context)


def new_component(request: Any) -> HttpResponse:
    return render(request, "cyclecomp/new_component.html")
