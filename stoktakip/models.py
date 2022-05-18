from statistics import mode
from django.db import models
# Create your models here.

class Product(models.Model):
    id          = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    countStock  = models.IntegerField()

    def __str__(self):
        return self.productName


class Store(models.Model):
    id        = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=50)

    def __str__(self):
        return self.storeName


class InStoreProducts(models.Model):
    storeName      = models.ForeignKey(Store,on_delete=models.CASCADE)
    salesProductId = models.IntegerField(unique=True)
    salesProducts  = models.ManyToManyField(Product)
    storeStock     = models.IntegerField()

    def __str__(self):
        return f"{self.storeName} - {self.salesProducts} - {self.storeStock}"


class SalesProducts(models.Model):
    storeName      = models.ForeignKey(Store,on_delete=models.CASCADE)
    salesProductId = models.IntegerField(unique=True)
    salesProducts  = models.ManyToManyField(Product)
    storeStock     = models.IntegerField()

    def __str__(self):
        return f"{self.storeName} - {self.salesProducts} - {self.storeStock}"