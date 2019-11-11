from django.db import models
from django.contrib.auth.models import User
class Coffees(models.Model):

    def __str__(self):
        return str(self.user) + ' ordered a ' + self.name + ', costs: ' + str(self.price)

    class Meta:
        verbose_name = 'Coffee'
        verbose_name_plural = 'Coffees'
        
    TEMPERATURES = [
        ('H', 'Hot'),
        ('C', 'Cold'),
        ('T', 'Tepid'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='The person who needs coffee')
    name = models.CharField(max_length=24, help_text='Name of beverage')
    temperature = models.CharField(max_length=1, choices=TEMPERATURES, help_text='The degree or intensity of heat present in the coffee')
    description = models.TextField(help_text='Appealing description of beverage')
    price = models.DecimalField(max_digits=4, decimal_places=2, help_text='The amount of money expected for the coffee')
    

