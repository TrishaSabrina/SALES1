from django.db import models

class Products(models.Model):
    Code = models.CharField(max_length=20, blank=True, null=True)
    Name = models.CharField(max_length=200, blank=True, null=True)
    Unit_measure = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
           app_label = "products"
           managed = True  
            