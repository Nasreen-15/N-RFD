from django.urls import path
from . import views

urlpatterns = [
    path("Report/", views.Report_form, name="Report"),
]
