from django.db import models
from django.db.models import Max
from django.utils import timezone
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.FloatField()
    bidding_increment = models.FloatField()

    @property
    def final_price(self):
        max_price= self.bids.aggregate(max_price=Max('price'))['max_price']
        if not max_price:
            return self.bidding_increment
        return max_price
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    seller = models.ForeignKey("seller.Seller", on_delete=models.CASCADE, related_name='items')
    
    @property
    def status(self):
        print(timezone.now())
        if timezone.now() < self.start_date:
            return "Pending"
        elif timezone.now() > self.end_date:
            return "Closed"
        else:
            return "Running"
        
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"Item({self.__str__()})"
    
class Bid(models.Model):
    buyer = models.ForeignKey("buyer.Buyer", on_delete=models.SET_NULL, null=True, related_name="bids")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name="bids")
    price = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"Bid(buyer: {self.buyer} | item: {self.item})"
    

class Winner(models.Model):
    seller = models.ForeignKey("seller.Seller", on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey("buyer.Buyer", on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)