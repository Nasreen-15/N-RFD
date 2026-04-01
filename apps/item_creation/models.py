from django.db import models

class ApplyTemplate(models.Model):
    id = models.AutoField(primary_key=True)

    template_name = models.CharField(max_length=100, db_column="type")

    item_category_code = models.CharField(max_length=50, null=True, db_column="item_category_code")
    costing_method = models.CharField(max_length=50, null=True, db_column="costing_method")
    inventory_posting_group = models.CharField(max_length=50, null=True, db_column="inventory_posting_group")
    price_profit_calculation = models.CharField(max_length=50, null=True, db_column="price_profit_calculation")
    gen_prod_posting_group = models.CharField(max_length=50, null=True, db_column="gen_prod_posting_group")
    replenishment_system = models.CharField(max_length=50, null=True, db_column="replenishment_system")

    qc_applicable = models.CharField(max_length=50, null=True, db_column="qc_applicable")
    manufacturing_policy = models.CharField(max_length=50, null=True, db_column="manufacturing_policy")
    assembly_policy = models.CharField(max_length=50, null=True, db_column="assembly_policy")
    reordering_policy = models.CharField(max_length=50, null=True, db_column="reordering_policy")

    include_inventory = models.CharField(max_length=50, null=True, db_column="include_inventory")
    gst_credit = models.CharField(max_length=50, null=True, db_column="gst_credit")
    flushing_method = models.CharField(max_length=50, null=True, db_column="flushing_method")

    template_applied = models.CharField(max_length=100, null=True, db_column="template_applied")
    rounding_precision = models.CharField(max_length=50, null=True, db_column="rounding_precision")
    gst_group_code = models.CharField(max_length=50, null=True, db_column="gst_group_code")

    class Meta:
        db_table = "tbl_applytemplate"
        managed = False

# --- Corrected Item Model ---

class Item(models.Model):
    customer_id = models.CharField(max_length=100, null=True, blank=True) # Added null=True
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    last_ecn_no = models.CharField(max_length=100, null=True, blank=True)
    search_item = models.CharField(max_length=255, null=True, blank=True)
    no = models.CharField(max_length=100, null=True, blank=True)
    template_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    base_unit_of_measure = models.CharField(max_length=50, null=True, blank=True)
    shelf_no = models.IntegerField(null=True, blank=True)
    cell = models.CharField(max_length=100, null=True, blank=True)
    cell_type = models.CharField(max_length=100, null=True, blank=True)
    item_category_code = models.CharField(max_length=100, null=True, blank=True)
    product_group_code = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    fixture_no = models.CharField(max_length=100, null=True, blank=True)
    no_of_meet = models.CharField(max_length=100, null=True, blank=True)
    no_of_parts = models.CharField(max_length=100, null=True, blank=True)
    revision_no = models.IntegerField(null=True, blank=True)
    cust_vender_code = models.CharField(max_length=100, null=True, blank=True)
    hsn_sac_code = models.CharField(max_length=100, null=True, blank=True)
    costing_method = models.CharField(max_length=100, null=True, blank=True)
    inventory_posting_group = models.CharField(max_length=100, null=True, blank=True)
    price_profit_calculation = models.CharField(max_length=100, null=True, blank=True)
    last_modified_date = models.DateField(null=True, blank=True)
    gen_prod_posting_group = models.CharField(max_length=100, null=True, blank=True)
    replenishment_system = models.CharField(max_length=100, null=True, blank=True)
    qc_applicable = models.CharField(max_length=100, null=True, blank=True)
    manufacturing_policy = models.CharField(max_length=100, null=True, blank=True)
    assembly_policy = models.CharField(max_length=100, null=True, blank=True)
    reordering_policy = models.CharField(max_length=100, null=True, blank=True)
    include_inventory = models.CharField(max_length=100, null=True, blank=True)
    gst_credit = models.CharField(max_length=100, null=True, blank=True)
    flushing_method = models.CharField(max_length=100, null=True, blank=True)
    template_applied = models.CharField(max_length=100, null=True, blank=True)
    rounding_precision = models.CharField(max_length=100, null=True, blank=True)
    gst_group_code = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "tbl_item"

    def __str__(self):
        return self.customer_name