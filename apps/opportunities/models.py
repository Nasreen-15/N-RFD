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