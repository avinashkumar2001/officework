from django.db import models

class Products(models.Model):
    name =  models.CharField(max_length=30)
    price = models.FloatField()
    stok = models.IntegerField()
    image_url = models.CharField(max_length=2038)

class Offer(models.Model):
    code=models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    discount = models.FloatField()
