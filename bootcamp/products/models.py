from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    number = models.IntegerField(null= True, blank=True)
