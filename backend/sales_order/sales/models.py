from django.db import models

class Sales(models.Model):
    customer = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True)
    product = models.CharField(max_length=200, blank=True, null=True)
    qty= models.CharField(max_length=20, blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    
    class Meta:
           app_label = "sales"
           managed = True  
            