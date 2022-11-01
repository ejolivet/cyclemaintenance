from django.urls import path

from . import views

app_name = "cyclecomp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<uuid:component_id>/", views.detail, name="detail"),
    path("define_component", views.define_component, name="define_component"),
    path("new_component", views.new_component, name="new_component"),
    path("define_component_api", views.define_component_api),
]
