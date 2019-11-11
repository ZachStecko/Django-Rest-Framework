from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import Coffees
from coldstartcase.serializers import CoffeeSerializer

# Create your views here.

class CoffeeViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Coffees.objects.all()
    serializer_class = CoffeeSerializer