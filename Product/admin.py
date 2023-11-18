from django.contrib import admin
from django import forms
from .models import Product, Order, Item



class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'price','created', 'last_updated','Rest_id']
    readonly_fields = ['slug', 'created', 'last_updated',]

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','count','cost','order_by', 'name','address', 'delivered', 'delivered_on', 'created', 'last_updated',]
    readonly_fields = ['slug','order_by', 'created', 'last_updated',]

admin.site.register(Order, OrderAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','item_name','item_desc','item_price','item_image','link_id']
    
admin.site.register(Item,ItemAdmin)


