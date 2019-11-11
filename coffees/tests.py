from django.test import TestCase
from .models import Coffees
from django.contrib.auth.models import User
# Create your tests here.

class CoffeeTest(TestCase):

    #Creates a coffee object
    def test_coffee(self):
        u = User(username='testuser', password='12345')
        u.save()

        Coffees.objects.create(
            name='Regular', temperature='H', description='My favorite coffee', price='2',
            user=u
        )

        testCoffee = Coffees.objects.get(user=u)

        self.assertEqual(str(testCoffee) , 'testuser ordered a Regular, costs: 2.00')

