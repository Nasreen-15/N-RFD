from django.urls import path
from . import views

urlpatterns = [
    path("feasibility_form/", views.feasibility, name="feasibility_form"),
]