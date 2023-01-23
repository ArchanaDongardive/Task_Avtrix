from django.db import models

# Create your models here.


class Product(models.Model):
    Order_date = models.DateField()
    Region = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Category = models.CharField(max_length=255)
    Product = models.CharField(max_length=200)
    Quantity = models.IntegerField()
    UnitPrice = models.FloatField()


    class Meta:
        db_table = "prod"




