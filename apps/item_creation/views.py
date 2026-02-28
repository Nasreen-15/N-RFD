from django.shortcuts import render

def item_creation_form(request):
    return render(request, "item_creation/item_creation_form.html")
