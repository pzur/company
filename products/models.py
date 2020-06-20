from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
     company = models.CharField(max_length=30, unique=True)
     ruc =models.IntegerField()
     web = models.CharField(max_length=120, unique=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="usuario")

     def __str__(self):
         return self.company

class Products (models.Model):
    product = models.CharField(max_length=30)
    sku = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2) 
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="company_product")

    def __str__(self):
        return self.product

