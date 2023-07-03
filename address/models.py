from django.db import models

# Create your models here.
class Address(models.Model):
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)