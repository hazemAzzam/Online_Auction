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
        extra_kwargs = {
            "title": {
                "required": False,
            },
            "description": {
                "required": False,
            },
            "starting_bid": {
                "required": False,
            },
            "bidding_increment": {
                "required": False,
            },
            "start_date": {
                "required": False,
            },
            "seller": {
                "required": False,
            },
        }
        

class Bid_Serializer(ModelSerializer):
    item = PrimaryKeyRelatedField(queryset=Item.objects.filter(start_date__lte=timezone.now(), end_date__gt=timezone.now()))
    class Meta:
        model=Bid
        fields="__all__"

class Winnder_Serializer(ModelSerializer):
    seller_name = StringRelatedField(source="seller", read_only=True)
    buyer_name = StringRelatedField(source="buyer", read_only=True)
    item_title = StringRelatedField(source="item", read_only=True)
    final_price = FloatField(source="item.final_price", read_only=True)
    class Meta:
        model=Winner
        fields="__all__"
        extra_kwargs= {
            "seller": {
                "write_only": True,
            },
            "buyer": {
                "write_only": True,
            },
            "item": {
                "write_only": True,
            }
        }
    def create(self, validate_data):
        winner, _ = Winner.objects.get_or_create(**validate_data)
        return winner