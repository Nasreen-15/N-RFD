# models.py
from django.db import models

class CustomerInfo(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    search_name = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_customerinfo"   # <-- exact table name in PostgreSQL

    def __str__(self):
        return self.customer_id
