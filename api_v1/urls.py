from rest_framework.routers import DefaultRouter
from member.views import *
from address.views import *
from seller.views import *
from buyer.views import *
from item.views import *
from category.views import *

from django.urls import path, include

router = DefaultRouter()
router.register('members', Member_View)
router.register('sellers', Seller_View)
router.register('buyers', Buyer_View)
router.register('items', Item_View)
router.register('bids', Bid_View)
router.register('categories', Category_View)

urlpatterns = [
    path('', include(router.urls))
]