from django.shortcuts import render
from .models import Opportunity

def opportunity_creation(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "add":
            Opportunity.objects.create(
                projectName=request.POST.get('projectName'),
                customerName=request.POST.get('customerName'),
                contactName=request.POST.get('contactName'),
                contactNo=request.POST.get('contactNo'),
                itemNo=request.POST.get('itemNo'),
                custId=request.POST.get('custId'),
                estimatedSalesPrice=request.POST.get('estimatedSalesPrice') or 0,
                nominatedPrice=request.POST.get('nominatedPrice') or 0,
                creationDate=request.POST.get('creationDate') or None,
                status=request.POST.get('status'),
                remarks=request.POST.get('remarks'),
            )

    return render(request, "opportunities/opportunity_creation.html")