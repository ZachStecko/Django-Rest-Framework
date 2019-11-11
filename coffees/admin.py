from django.contrib import admin
from .models import Coffees


class CoffeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coffees, CoffeeAdmin)