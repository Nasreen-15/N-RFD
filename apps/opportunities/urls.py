from django.urls import path
from . import views

urlpatterns = [
    path("opportunity/", views.opportunity_creation, name="opportunity_creation"),
    path('opportunity_creation/', views.opportunity_creation, name='opportunity_creation'),
    path('get_item_numbers/', views.get_item_numbers, name='get_item_numbers'),
    path('get_salespersons/', views.get_salespersons, name='get_salespersons'),
    path('get_sales_cycles/', views.get_sales_cycles, name='get_sales_cycles'),
    path('get_segments/', views.get_segments, name='get_segments'),
    path('get_opportunity_details/', views.get_opportunity_details, name='get_opportunity_details'),
]
