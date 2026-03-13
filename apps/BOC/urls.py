from django.urls import path
from . import views

urlpatterns = [
    path("BOC/", views.BOC_form, name="BOC"),
]