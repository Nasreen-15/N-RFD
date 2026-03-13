from django.urls import path
from . import views

urlpatterns = [
    path("CostingBCCal/", views.CostingBCCal_form, name="CostingBCCal"),
]