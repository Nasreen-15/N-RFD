from django.urls import path
from . import views

urlpatterns = [
    path("item_creation/", views.item_creation_form, name="item_creation"),
    path("get_template_data/", views.get_template_data, name="get_template_data"),
]