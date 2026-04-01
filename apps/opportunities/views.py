from django.http import JsonResponse
from django.shortcuts import render
from .models import Opportunity
from apps.item_creation.models import ItemCard
from .models import CustomerInfo, OppSalesPeople, OppSalesCycles, OppSegment, OpportunityMaster, OpportunityMasterECN
from django.utils.timezone import now
from django.db.models import Max



# ✅ existing view (keep as it is)
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
            return redirect(request.path)

    return render(request, "opportunities/opportunity_creation.html", {
        "selected_customer_id": customer_id,
        "selected_customer_name": customer_name,
    })

def get_item_numbers(request):
    customer_id = request.GET.get("customer_id", "")

    if not customer_id:
        return JsonResponse({"data": [], "city": "", "contact": "", "creation_date": ""})

    items = ItemCard.objects.filter(customer_id=customer_id)
    numbers = list(items.values_list("no", flat=True))

    customer = CustomerInfo.objects.filter(customer_id=customer_id).first()

    city = ""
    contact = ""
    creation_date = now().strftime("%Y-%m-%d")

    if customer:
        city = customer.city or ""
        contact = customer.contact or ""

    return JsonResponse({
        "data": numbers,
        "city": city,
        "contact": contact,
        "creation_date": creation_date
    })

def get_salespersons(request):
    data = OppSalesPeople.objects.all().values("code", "name")

    result = [
        {"code": d["code"], "name": d["name"]}
        for d in data
    ]

    return JsonResponse({"data": result})

def get_sales_cycles(request):
    data = OppSalesCycles.objects.all().values(
        "code", "description", "probability_calculation"
    )

    result = [
        {
            "code": d["code"],
            "description": d["description"],
            "probability": d["probability_calculation"]
        }
        for d in data
    ]

    return JsonResponse({"data": result})

def get_segments(request):
    data = OppSegment.objects.all().values("no", "description")

    result = [
        {
            "no": d["no"],
            "description": d["description"]
        }
        for d in data
    ]

    return JsonResponse({"data": result})


def get_opportunity_details(request):
    val = request.GET.get("item_no", "").strip()

    if not val:
        return JsonResponse({"status": "error"}, status=400)

    try:
        opportunity = OpportunityMaster.objects.filter(item_no=val).values().first()

        if not opportunity and not val.startswith('0'):
            opportunity = OpportunityMaster.objects.filter(item_no='0'+val).values().first()

        if opportunity:
            # ✅ FETCH LAST ECN (IMPORTANT)
            last_ecn = OpportunityMasterECN.objects.filter(
                item_no=opportunity["item_no"]
            ).order_by("-ecn_id").values_list("ecn_id", flat=True).first()

            opportunity["last_ecn_no"] = last_ecn

            # format dates
            for key, value in opportunity.items():
                if hasattr(value, 'strftime') and value:
                    opportunity[key] = value.strftime('%Y-%m-%d')

            return JsonResponse({"status": "success", "data": opportunity})

        return JsonResponse({"status": "error", "message": "Not found"}, status=404)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

