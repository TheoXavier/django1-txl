from django.contrib import admin
from .models import Product, Client


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
