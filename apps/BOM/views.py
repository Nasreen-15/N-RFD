from django.shortcuts import render

def BOM_form(request):
    return render(request, "BOM/BOM_form.html")
