from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework import routers
from orders.views import OrderViewSet, PlaceOrderViewSet

router = routers.DefaultRouter()

router.register(r'place-order', PlaceOrderViewSet, 'place-order')
router.register(r'orders-list', OrderViewSet, 'orders-list')

urlpatterns = router.urls