from django.shortcuts import render

def feasibility(request):
    return render(request, "feasibility_form/feasibility.html")
