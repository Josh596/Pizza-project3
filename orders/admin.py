from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Menu)
admin.site.register(Items)
admin.site.register(Toppings)
admin.site.register(Item_price)
admin.site.register(Add_ons)
admin.site.register(Size)
admin.site.register(Order)