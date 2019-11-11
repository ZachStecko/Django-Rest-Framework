from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from coffees.models import Coffees
from .models import Orders
from coldstartcase.serializers import OrderSerializer, PlaceOrderSerializer
from django.db.models import Sum
# Create your views here.

#A viewset to view the orders that have been placed
class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

#A viewset to place orders 
class PlaceOrderViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Orders.objects.all()
    serializer_class = PlaceOrderSerializer
    
    #Sum up the total price of all the coffees for an order
    def perform_create(self, serializer):
        if self.request.method == 'POST':
            totalAmount = 0
            for x in self.request.POST.getlist('coffee'):
                obj = Coffees.objects.get(id=x)
                price = getattr(obj,'price')
                totalAmount += price

            serializer.save(total=totalAmount)