from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Item_View(ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=Item_Serializer

class Bid_View(ModelViewSet):
    queryset=Bid.objects.all()
    serializer_class=Bid_Serializer