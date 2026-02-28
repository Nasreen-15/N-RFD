from django.shortcuts import render

def customer_form(request):
    return render(request, "customer_creation/customer_form.html")
