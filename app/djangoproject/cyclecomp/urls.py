from django.urls import path

from . import views

app_name = "cyclecomp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:component_id>/", views.detail, name="detail"),
    path("define_component", views.define_component),
]
