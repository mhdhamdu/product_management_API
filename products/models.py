from django.db import models

# Create your models here.

class Product(models.Model):
    product_code = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product_code
