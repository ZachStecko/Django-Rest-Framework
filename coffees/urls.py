from . import views
from django.contrib import admin
from rest_framework import routers
from coffees.views import CoffeeViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'request-coffee', CoffeeViewSet,'request-coffee')

urlpatterns = router.urls