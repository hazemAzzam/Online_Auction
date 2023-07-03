from rest_framework.customs import ComplexSerializer
from member.serializers import *
from .models import *

class Buyer_Serializer(Member_Serializer):
    shipping_address = Address_Serializer(required=False, many=True)
    class Meta(Member_Serializer.Meta):
        model=Buyer
        fields="__all__"

