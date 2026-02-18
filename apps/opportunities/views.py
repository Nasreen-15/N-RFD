from django.shortcuts import render

def opportunity_creation(request):
    return render(request, "opportunities/opportunity_creation.html")
