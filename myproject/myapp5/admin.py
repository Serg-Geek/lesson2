from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    """Списрк продуктов"""
    list_display = ['name', 'category', 'quantity', ]
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# Register your models here.
