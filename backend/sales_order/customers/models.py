from django.db import models

class Customers(models.Model):
    Code = models.CharField(max_length=20, blank=True, null=True)
    Name = models.CharField(max_length=200, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
           app_label = "customers"
           managed = True 