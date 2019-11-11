from django.test import TestCase
from .models import Orders
from coffees.models import Coffees
from datetime import datetime 
from django.contrib.auth.models import User
from pprint import pprint
# Create your tests here.
class OrderTest(TestCase):

    #Creates a test user then adds a coffee order, testing to see if it's valid
    def test_order(self):
        u1 = User(username='testuser1', password='12345')
        u1.save()

        #Coffee order 1
        Coffees.objects.create(
            name='Regular', temperature='H', description='My favorite coffee', price='2.21',
            user=u1
        )

        #Coffee order 2
        u2 = User(username='testuser2', password='12345')
        u2.save()

        Coffees.objects.create(
            name='Double Double', temperature='H', description='An ok coffee', price='3.37',
            user=u2
        )

        #Create order object
        users = Coffees.objects.all()
        totalAmount = 0

        #Get total price
        for x in range(3):
            ob = Coffees.objects.filter(id=x).values()
            for i in ob:
                price = i['price']
                totalAmount += price

        #Create the object
        obj = Orders.objects.create(
            date=datetime.now(), total=totalAmount
        )
        obj.coffee.set(users)

        pprint(vars(obj))