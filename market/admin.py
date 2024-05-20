from django.contrib import admin

from .models import Goods, Delivery
# Register your models here.


admin.site.register(Delivery)
admin.site.register(Goods)