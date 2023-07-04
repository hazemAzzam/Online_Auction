from rest_framework.serializers import  ModelSerializer, FloatField, CharField, PrimaryKeyRelatedField, SlugField, StringRelatedField
from .models import *
from seller.models import Seller
from buyer.models import Buyer


class Item_Serializer(ModelSerializer):
    final_price = CharField(read_only=True)
    status = CharField(read_only=True)
    class Meta:
        model=Item
        fields="__all__"
        

class Bid_Serializer(ModelSerializer):
    item = PrimaryKeyRelatedField(queryset=Item.objects.filter(start_date__lte=timezone.now(), end_date__gt=timezone.now()))
    class Meta:
        model=Bid
        fields="__all__"

class Winnder_Serializer(ModelSerializer):
    seller = StringRelatedField()
    buyer = StringRelatedField()
    item = StringRelatedField()
    final_price = FloatField(source="item.final_price", read_only=True)
    class Meta:
        model=Winner
        fields="__all__"