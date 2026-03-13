from django.shortcuts import render

def BOP_form(request):
    return render(request, "BOP/BOP_form.html")
