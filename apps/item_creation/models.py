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