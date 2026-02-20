from django.urls import path
from . import views

urlpatterns = [
    path("erp-data/", views.erp_data_view, name="erp_data"),
    path("upload-data/", views.upload_data_view, name="upload_data"),
    path("user-management/", views.user_management_view, name="user_management"),
]