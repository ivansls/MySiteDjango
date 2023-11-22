from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'discription')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'discription')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'discription', 'photo', 'price', 'category', 'exist')


@admin.register(Order_item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number_of_products_per_position', 'discount_per_item')


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'unique_number', 'delivery_address', 'client_phone_number', 'Clients_full_name')