from django.urls import path
from . import views

urlpatterns = [
    path("BlanketSales/", views.BlanketSales_form, name="BlanketSales"),
]