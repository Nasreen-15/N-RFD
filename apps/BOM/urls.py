from django.urls import path
from . import views

urlpatterns = [
    path("BOM/", views.BOM_form, name="BOM"),
]