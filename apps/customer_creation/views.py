# views.py
from django.shortcuts import render
from .models import CustomerInfo

def customer_form(request):
    customer_ids = CustomerInfo.objects.values_list("customer_id", flat=True)
    search_names = CustomerInfo.objects.values_list("search_name", flat=True)

    return render(
        request,
        "customer_creation/customer_form.html",
        {
            "customer_ids": customer_ids,
            "search_names": search_names,
        }
    )
