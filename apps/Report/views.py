from django.shortcuts import render

def Report_form(request):
    return render(request, "Report/Report_form.html")
