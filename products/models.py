from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    feedbacks = models.IntegerField()
    basic_price = models.IntegerField()
    discount_price = models.IntegerField()
    wb_wallet_price = models.IntegerField()
