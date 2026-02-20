from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erp-data/', views.erp_data, name='erp_data'),
   path('upload-data/', views.upload_data, name='upload_data'),

]
