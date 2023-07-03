from django.db import models
from member.models import Member

# Create your models here.
class Seller(Member):
    bank_account_number = models.CharField(max_length=50)
    routing_number = models.IntegerField()