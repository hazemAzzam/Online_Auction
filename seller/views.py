from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class Seller_View(ModelViewSet):
    queryset=Seller.objects.all()
    serializer_class=Seller_Serializer