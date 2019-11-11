from django.db import models
from django.db.models import Sum
from coffees.models import Coffees
# Create your models here.

class Orders(models.Model):
    
    #Order object accepts multiple coffee objects and then adds up the total cost
    coffee = models.ManyToManyField(Coffees,help_text='Choose which coffee requests you want to add to your order')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    total = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order ' + str(self.id) + ' - Price: ' + str(self.total)
