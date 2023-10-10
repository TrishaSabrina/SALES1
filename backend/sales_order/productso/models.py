from django.db import models

class Productso(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
           app_label = "products"
           managed = True  
            