from django.urls import path
from . import views

urlpatterns = [
    path("opportunity/", views.opportunity_creation, name="opportunity_creation"),
]
