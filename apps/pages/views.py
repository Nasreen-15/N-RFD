from django.shortcuts import render
from django.utils import timezone
print(">>> LOADING apps.pages.views <<<")

def index(request):
    return render(request, 'pages/index.html')

def erp_data_view(request):
    current_date = timezone.now().strftime("%d-%b-%y")
    return render(request, 'pages/erp_data.html', {"current_date": current_date})

def upload_data_view(request):
    return render(request, "pages/upload_data.html")

def user_management_view(request):
    return render(request, "pages/user_management.html")
