from django.db import models

# Create your models here.
class Opportunity(models.Model):
    projectName = models.CharField(max_length=255, null=True, blank=True)
    customerName = models.CharField(max_length=255, null=True, blank=True)
    contactName = models.CharField(max_length=255, null=True, blank=True)
    contactNo = models.CharField(max_length=20, null=True, blank=True)
    
    itemNo = models.CharField(max_length=100, null=True, blank=True)
    custId = models.CharField(max_length=100, null=True, blank=True)

    estimatedSalesPrice = models.FloatField(default=0)
    nominatedPrice = models.FloatField(default=0)

    creationDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.projectName or "Opportunity"
    
class ItemCard(models.Model):
    no = models.CharField(max_length=50, primary_key=True, db_column="no")
    customer_id = models.CharField(max_length=50, db_column="customer_id")

    class Meta:
        db_table = "tbl_itemcard"
        managed = False

class CustomerInfo(models.Model):
    customer_id = models.CharField(max_length=50, primary_key=True, db_column="customer_id")
    city = models.CharField(max_length=100, blank=True, null=True, db_column="city")
    contact = models.CharField(max_length=255, db_column="contact")

    class Meta:
        db_table = "tbl_customerinfo"
        managed = False

class OppSalesPeople(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="code")
    name = models.CharField(max_length=255, db_column="name")

    class Meta:
        db_table = "tbl_oppsalespeople"
        managed = False

class OppSalesCycles(models.Model):
    code = models.CharField(max_length=50, primary_key=True, db_column="Code")
    description = models.CharField(max_length=255, db_column="Description")
    probability_calculation = models.CharField(max_length=100, db_column="Probability_Calculation")

    class Meta:
        db_table = "tbl_oppsalescycles"
        managed = False

class OppSegment(models.Model):
    no = models.CharField(max_length=50, primary_key=True, db_column="no")
    description = models.CharField(max_length=255, db_column="description")

    class Meta:
        db_table = "tbl_oppsegment"
        managed = False

class OpportunityMaster(models.Model):
    item_no = models.CharField(max_length=50, primary_key=True, db_column="item_no")

    opportunity_id = models.CharField(max_length=50, db_column="id", null=True, blank=True)
    last_ecn_no = models.CharField(max_length=50, db_column="no_2", null=True, blank=True)

    project_name_db = models.CharField(max_length=255, db_column="description", null=True, blank=True)
    customer_id = models.CharField(max_length=50, db_column="customerid", null=True, blank=True)
    customer_name_db = models.CharField(max_length=255, db_column="customername", null=True, blank=True)

    contact_name = models.CharField(max_length=255, db_column="contactname", null=True, blank=True)
    contact_no = models.CharField(max_length=50, db_column="contact_no", null=True, blank=True)

    salesperson_code = models.CharField(max_length=50, db_column="salesperson_code", null=True, blank=True)
    sales_cycle_code = models.CharField(max_length=50, db_column="sales_cycle_code", null=True, blank=True)

    creation_date = models.DateField(db_column="creation_date", null=True, blank=True)
    status = models.CharField(max_length=50, db_column="status", null=True, blank=True)
    reason = models.CharField(max_length=100, db_column="reason", null=True, blank=True)

    segment_no = models.CharField(max_length=50, db_column="segment_no", null=True, blank=True)
    segment_desc = models.CharField(max_length=255, db_column="segment_description", null=True, blank=True)

    part_name = models.CharField(max_length=255, db_column="part_name", null=True, blank=True)

    opp_received_date = models.DateField(db_column="opportunity_received_date", null=True, blank=True)
    sop_date = models.DateField(db_column="sop_date", null=True, blank=True)

    drawing_rev = models.CharField(max_length=50, db_column="drawing_revision_no", null=True, blank=True)
    application = models.CharField(max_length=100, db_column="application", null=True, blank=True)
    business = models.CharField(max_length=100, db_column="business", null=True, blank=True)
    plant_loc = models.CharField(max_length=100, db_column="voss_plant_location", null=True, blank=True)

    status_date = models.DateField(db_column="status_date", null=True, blank=True)
    sales_goahead = models.DateField(db_column="sales_goahead_date_for_tool", null=True, blank=True)

    vol1 = models.CharField(max_length=50, db_column="annual_volume", null=True, blank=True)
    year1 = models.CharField(max_length=50, db_column="annual_volume_year", null=True, blank=True)
    vol2 = models.CharField(max_length=50, db_column="annual_volume_2", null=True, blank=True)
    year2 = models.CharField(max_length=50, db_column="annual_volume_year_2", null=True, blank=True)
    vol3 = models.CharField(max_length=50, db_column="annual_volume_3", null=True, blank=True)
    year3 = models.CharField(max_length=50, db_column="annual_volume_year_3", null=True, blank=True)
    vol4 = models.CharField(max_length=50, db_column="annual_volume_4", null=True, blank=True)
    year4 = models.CharField(max_length=50, db_column="annual_volume_year_4", null=True, blank=True)
    vol5 = models.CharField(max_length=50, db_column="annual_volume_5", null=True, blank=True)
    year5 = models.CharField(max_length=50, db_column="annual_volume_year_5", null=True, blank=True)

    est_price = models.FloatField(db_column="part_price_1", null=True, blank=True)
    est_val = models.FloatField(db_column="estimated_value", null=True, blank=True)
    euro_conv = models.FloatField(db_column="estimated_euro_conv", null=True, blank=True)

    life_cycle = models.CharField(max_length=50, db_column="life_cycle_in_years", null=True, blank=True)

    remarks = models.TextField(db_column="remarks", null=True, blank=True)
    quote_status = models.CharField(max_length=50, db_column="quotestatus", null=True, blank=True)
    cat_type = models.CharField(max_length=50, db_column="categorytype", null=True, blank=True)

    modified_date = models.DateField(db_column="last_modified_date", null=True, blank=True)

    class Meta:
        db_table = "tbl_opportunitymaster"
        managed = False

class OpportunityMasterECN(models.Model):
    item_no = models.CharField(max_length=50, db_column="item_no")
    ecn_id = models.CharField(max_length=50, db_column="ecn_id")

    class Meta:
        db_table = "tbl_opportunitymaster_ecn"
        managed = False
