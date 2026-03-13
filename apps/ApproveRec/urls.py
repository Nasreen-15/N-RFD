from django.urls import path
from . import views

urlpatterns = [
    path("ApproveRec/", views.ApproveRec_form, name="ApproveRec"),
]