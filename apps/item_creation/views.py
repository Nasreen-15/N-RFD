

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ApplyTemplate, Item  # Make sure Item is here

def item_creation_form(request):
    # --- BLOCK TO ADD DATA TO DATABASE ---
    if request.method == "POST":
        Item.objects.create(
            customer_id=request.POST.get('customer_id'),
            customer_name=request.POST.get('customer_name'),
            last_ecn_no=request.POST.get('lastEcnNo'),
            search_item=request.POST.get('s_item'),
            no=request.POST.get('no'),
            template_name=request.POST.get('templatename'),
            description=request.POST.get('description'),
            base_unit_of_measure=request.POST.get('base_unit_of_measure'),
            # 'or None' prevents errors if these numeric/date fields are empty
            shelf_no=request.POST.get('shelf_no') or None, 
            cell=request.POST.get('cell'),
            cell_type=request.POST.get('cell_type'),
            item_category_code=request.POST.get('item_category_code'),
            product_group_code=request.POST.get('product_group_code'),
            status=request.POST.get('status'),
            fixture_no=request.POST.get('fixture'),
            no_of_meet=request.POST.get('noofmeet'),
            no_of_parts=request.POST.get('noofparts'),
            revision_no=request.POST.get('revision') or None,
            cust_vender_code=request.POST.get('custVenderCode'),
            hsn_sac_code=request.POST.get('hsn'),
            costing_method=request.POST.get('costingmethod'),
            inventory_posting_group=request.POST.get('inventory'),
            price_profit_calculation=request.POST.get('priceprofit'),
            last_modified_date=request.POST.get('lastModifiedDate') or None,
            gen_prod_posting_group=request.POST.get('genpro'),
            replenishment_system=request.POST.get('replenishment'),
            qc_applicable=request.POST.get('qc'),
            manufacturing_policy=request.POST.get('manu'),
            assembly_policy=request.POST.get('assembly'),
            reordering_policy=request.POST.get('reordering'),
            include_inventory=request.POST.get('inventoryinclude'),
            gst_credit=request.POST.get('gst'),
            flushing_method=request.POST.get('flushing'),
            template_applied=request.POST.get('template_applied'),
            rounding_precision=request.POST.get('rounding'),
            gst_group_code=request.POST.get('gstgroup'),
        )
        # Redirect back to the same page or a success page
        return redirect(request.path)

    # --- EXISTING GET LOGIC ---
    selected_customer_id = request.GET.get("customer_id")
    selected_name = request.GET.get("name")
    template_names = ApplyTemplate.objects.values_list("template_name", flat=True)

    return render(request, "item_creation/item_creation_form.html", {
        "template_name": template_names,
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