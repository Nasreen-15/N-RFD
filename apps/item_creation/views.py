

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ApplyTemplate


def item_creation_form(request):

    # ✅ GET FROM CUSTOMER PAGE
    selected_customer_id = request.GET.get("customer_id")
    selected_name = request.GET.get("name")

    # ✅ ONLY TEMPLATE DATA
    template_names = ApplyTemplate.objects.values_list("template_name", flat=True)

    # ✅ FETCH UOM DATA
    uoms = UnitOfMeasure.objects.all()
    item_categories = ItemCategory.objects.all()
    product_groups = ProductGroup.objects.all()
    cells = Cell.objects.all()
    hsn_codes = HSNCode.objects.all()
    cell_types = CellType.objects.all()

    items = []
    first_item_no = ""
    if selected_customer_id:
        items = list(ItemCard.objects.filter(customer_id=selected_customer_id).values_list("no", flat=True))
        if items:
            first_item_no = items[0]

    return render(request, "item_creation/item_creation_form.html", {
        "template_name": template_names,

        # ✅ PASS CUSTOMER DATA
        "selected_customer_id": selected_customer_id,
        "selected_name": selected_name,
        "first_item_no": first_item_no,
    })

def get_template_data(request):
    template_name = request.GET.get("template_name", "")
    try:
        t = ApplyTemplate.objects.get(template_name=template_name)
        return JsonResponse({
            "item_category_code": getattr(t, 'item_category_code', "") or "",
            "costing_method": getattr(t, 'costing_method', "") or "",
            "inventory_posting_group": getattr(t, 'inventory_posting_group', "") or "",
            "price_profit_calculation": getattr(t, 'price_profit_calculation', "") or "",
            "gen_prod_posting_group": getattr(t, 'gen_prod_posting_group', "") or "",
            "replenishment_system": getattr(t, 'replenishment_system', "") or "",
            "qc_applicable": getattr(t, 'qc_applicable', "") or "",
            "manufacturing_policy": getattr(t, 'manufacturing_policy', "") or "",
            "assembly_policy": getattr(t, 'assembly_policy', "") or "",
            "reordering_policy": getattr(t, 'reordering_policy', "") or "",
            "include_inventory": getattr(t, 'include_inventory', "") or "",
            "gst_credit": getattr(t, 'gst_credit', "") or "",
            "flushing_method": getattr(t, 'flushing_method', "") or "",
            "template_applied": getattr(t, 'template_name', "") or "",
            "rounding_precision": getattr(t, 'rounding_precision', "") or "",
            "gst_group_code": getattr(t, 'gst_group_code', "") or "",
        })
    except ApplyTemplate.DoesNotExist:
        return JsonResponse({"error": "Template not found"}, status=404)
    except Exception as e:
        logger.exception("Error in get_template_data for %s", template_name)
        return JsonResponse({"error": str(e)}, status=500)

def get_item_details(request):
    item_no = request.GET.get("item_no", "").strip()
    cust_id = request.GET.get("customer_id", "").strip()

    if not item_no:
        return JsonResponse({"error": "Missing item_no"}, status=400)

    query = {"no": item_no}
    if cust_id:
        query["customer_id"] = cust_id

    try:
        item = ItemCard.objects.filter(**query).first()

        if not item:
            return JsonResponse({"error": "Item not found"}, status=404)

        # Handle date separately (same as before but compact)
        last_modified = ""
        if getattr(item, "lastModifiedDate", None):
            try:
                if hasattr(item.lastModifiedDate, "strftime"):
                    last_modified = item.lastModifiedDate.strftime("%Y-%m-%d")
                else:
                    last_modified = str(item.lastModifiedDate)
            except Exception:
                last_modified = ""

        return JsonResponse({
            "no": getattr(item, "no", "") or "",
            "description": getattr(item, "description", "") or "",
            "base_unit_of_measure": getattr(item, "base_unit_of_measure", "") or "",
            "shelf_no": getattr(item, "shelf_no", "") or "",
            "cell": getattr(item, "cell", "") or "",
            "cell_type": getattr(item, "cell_type", "") or "",
            "item_category_code": getattr(item, "item_category_code", "") or "",
            "product_group_code": getattr(item, "product_group_code", "") or "",
            "status": getattr(item, "status", "") or "",
            "fixture": getattr(item, "fixture", "") or "",
            "noofparts": getattr(item, "noofparts", "") or "",
            "noofmeet": getattr(item, "noofmeet", "") or "",
            "revision": getattr(item, "revision", "") or "",
            "custVenderCode": getattr(item, "custVenderCode", "") or "",
            "hsn": getattr(item, "hsn", "") or "",
            "lastModifiedDate": last_modified
        })

    except Exception as e:
        logger.exception("Error in get_item_details for %s", item_no)
        return JsonResponse({"error": str(e)}, status=500)