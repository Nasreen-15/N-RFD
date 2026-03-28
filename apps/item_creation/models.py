from django.db import models

class ApplyTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    # db_column="type" matches your existing table logic
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

class ItemCard(models.Model):
    no = models.CharField(max_length=50, primary_key=True, db_column="no")
    customer_id = models.CharField(max_length=50, db_column="customerid", null=True)
    description = models.CharField(max_length=255, db_column="description", null=True)
    
    # Fields to fix
    base_unit_of_measure = models.CharField(max_length=50, db_column="base_unit_of_measure", null=True)
    cell = models.CharField(max_length=50, db_column="cell", null=True)
    cell_type = models.CharField(max_length=50, db_column="cell_type", null=True)
    item_category_code = models.CharField(max_length=50, db_column="item_category_code", null=True)
    product_group_code = models.CharField(max_length=50, db_column="product_group_code", null=True)
    status = models.CharField(max_length=50, db_column="status", null=True)
    
    # Matching your provided column list exactly
    fixture = models.CharField(max_length=50, db_column="fixture_no", null=True)
    noofparts = models.CharField(max_length=50, db_column="no_of_parts", null=True) 
    noofmeet = models.CharField(max_length=50, db_column="no_of_meft", null=True)
    revision = models.CharField(max_length=50, db_column="revision_no", null=True)
    custVenderCode = models.CharField(max_length=50, db_column="customer_vendor_code", null=True)
    hsn = models.CharField(max_length=50, db_column="hsn_sac_code", null=True)
    lastModifiedDate = models.DateTimeField(db_column="last_date_modified", null=True)

    class Meta:
        db_table = "tbl_itemcard"
        managed = False

class UnitOfMeasure(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")
    description = models.CharField(max_length=255, db_column="description")

    class Meta:
        db_table = "tbl_unitsofmeasure"
        managed = False

class ItemCategory(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")
    description = models.CharField(max_length=255, db_column="description")
    def_gen_prod_posting_group = models.CharField(max_length=50, db_column="def_gen_prod_posting_group", null=True)

    class Meta:
        db_table = "tbl_itemcategories"
        managed = False

class ProductGroup(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")

    class Meta:
        db_table = "tbl_productgroups"
        managed = False


class Cell(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")

    class Meta:
        db_table = "tbl_cell"
        managed = False


class CellType(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")

    class Meta:
        db_table = "tbl_celltype"
        managed = False

class HSNCode(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")

    class Meta:
        db_table = "tbl_itemcard_invoice"
        managed = False