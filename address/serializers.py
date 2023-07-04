from Online_Auction.ComplexSerializer import *
from .models import *

class Address_Serializer(ComplexSerializer):
    class Meta:
        model=Address
        fields="__all__"