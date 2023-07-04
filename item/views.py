from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import action
from django.db.models import Max, Q
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .filters import Items_Filter


class Item_View(ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=Item_Serializer
    filterset_class=Items_Filter

    @action(detail=False, methods=['GET'])
    def running(self, request):
        return Response(Item_Serializer(instance=Item.objects.filter(start_date__lte=timezone.now(), end_date__gt=timezone.now()), many=True).data)

    @action(detail=False, methods=['GET'])
    def pending(self, request):
        return Response(
            Item_Serializer(
                instance=Item.objects.filter(
                    start_date__gt=timezone.now()
                ),
                many=True
            ).data
        )
    
    @action(detail=False, methods=['GET'])
    def closed(self, request):
        return Response(
            Item_Serializer(
                instance=Item.objects.filter(
                    end_date__lt=timezone.now()
                ),
                many=True
            ).data
        )
    
    @action(detail=True, methods=['GET'])
    def end_bid(self, request, pk=None):
        item = Item.objects.get(id=pk)
        if item.status == "Closed":
            try:
                buyer = Bid.objects.get(item=pk, price=item.final_price).buyer
            except:
                return Response({"message": "This item has no buyers"})
            seller = item.seller
            winner = Winnder_Serializer(data={"item": item.pk, "buyer": buyer.id, "seller": seller.id})
            winner.is_valid(raise_exception=True)
            winner_instance = winner.save()
            return(Response(winner.data))
        else:
            return Response({"message": "This item is still running!"})

class Bid_View(ModelViewSet):
    queryset=Bid.objects.all()
    serializer_class=Bid_Serializer

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        item = data['item']
        price = data['price']
        item_instance = Item.objects.get(id=item)
        if timezone.now() < item_instance.end_date:
            if (price - item_instance.final_price) >= item_instance.bidding_increment:
                bid_serializer = Bid_Serializer(data=data)
                bid_serializer.is_valid(raise_exception=True)

                bid_serializer.save()
                return Response(Item_Serializer(instance=item_instance).data)
        else:
            return Response({"message": f"this item is closed."})

        return Response({"message": f"your bidding increment must be bigger than {item_instance.bidding_increment}"})

class Winnder_View(ModelViewSet):
    queryset=Winner.objects.all()
    serializer_class=Winnder_Serializer