from django.contrib import admin
from .models import Client, Product, Order, Category


class ProductAdmin(admin.ModelAdmin):
    """Списрк продуктов"""
    list_display = ['name', 'category', 'quantity', ]
    ordering = ['category', '-quantity']
    list_filter = ['price', 'added_date', 'category']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Client)

# Register your models here.
