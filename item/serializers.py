from rest_framework.customs import  ModelSerializer
from .models import *

class Item_Serializer(ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"

class Bid_Serializer(ModelSerializer):
    class Meta:
        model=Bid
        fields="__all__"