from django.urls import path
from . import views

urlpatterns = [
    path("BOP/", views.BOP_form, name="BOP"),
]