from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.FloatField()
    bidding_increment = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    seller = models.ForeignKey("seller.Seller", on_delete=models.CASCADE, related_name='items')
    
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