from django.shortcuts import render
from django.http import JsonResponse
from .models import ApplyTemplate


def item_creation_form(request):

    # ✅ GET FROM CUSTOMER PAGE
    selected_customer_id = request.GET.get("customer_id")
    selected_name = request.GET.get("name")

    # ✅ ONLY TEMPLATE DATA
    template_names = ApplyTemplate.objects.values_list("template_name", flat=True)

    return render(request, "item_creation/item_creation_form.html", {
        "template_name": template_names,

        # ✅ PASS CUSTOMER DATA
        "selected_customer_id": selected_customer_id,
        "selected_name": selected_name,
    })


# ✅ TEMPLATE FETCH API
def get_template_data(request):
    template_name = request.GET.get("template_name")

    try:
        t = ApplyTemplate.objects.get(template_name=template_name)

        return JsonResponse({
            "item_category_code": t.item_category_code,
            "costing_method": t.costing_method,
            "inventory_posting_group": t.inventory_posting_group,
            "price_profit_calculation": t.price_profit_calculation,
            "gen_prod_posting_group": t.gen_prod_posting_group,
            "replenishment_system": t.replenishment_system,
            "qc_applicable": t.qc_applicable,
            "manufacturing_policy": t.manufacturing_policy,
            "assembly_policy": t.assembly_policy,
            "reordering_policy": t.reordering_policy,
            "include_inventory": t.include_inventory,
            "gst_credit": t.gst_credit,
            "flushing_method": t.flushing_method,
            "template_applied": t.template_name,
            "rounding_precision": t.rounding_precision,
            "gst_group_code": t.gst_group_code,
        })

    except ApplyTemplate.DoesNotExist:
        return JsonResponse({"error": "Template not found"}, status=404)