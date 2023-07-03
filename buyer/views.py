from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class Buyer_View(ModelViewSet):
    queryset=Buyer.objects.all()
    serializer_class=Buyer_Serializer