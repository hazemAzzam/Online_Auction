from .models import *
from member.serializers import *

class Seller_Serializer(Member_Serializer):
    
    class Meta(Member_Serializer.Meta):
        model = Seller
        fields="__all__"