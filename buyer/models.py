from django.db import models
from member.models import Member

# Create your models here.
class Buyer(Member):
    shipping_address = models.ManyToManyField("address.Address")
