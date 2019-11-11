from rest_framework import serializers
from django.db.models import Sum
from django.contrib.auth.models import User
from coffees.models import Coffees
from orders.models import Orders

#Serializers

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffees
        fields = ('user','name','temperature','description','price')

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('coffee', 'date')

class OrderSerializer(serializers.ModelSerializer):
    coffee = CoffeeSerializer(many=True)
    class Meta:
        model = Orders
        fields = ('coffee','date','total')

    