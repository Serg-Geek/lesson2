from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from myproject.hw_2app.models import Product
# from .models import Product

def product_list(request):
    # Получаем текущую дату и часовой пояс
    current_date = timezone.now()

    # Определяем даты для фильтрации (7 дней, 30 дней и 365 дней назад)
    week_ago = current_date - timedelta(days=7)
    month_ago = current_date - timedelta(days=30)
    year_ago = current_date - timedelta(days=365)

    # Фильтруем заказы по дате и выбираем только уникальные товары
    week_products = Product.objects.filter(order__order_date__gte=week_ago).distinct()
    month_products = Product.objects.filter(order__order_date__gte=month_ago).distinct()
    year_products = Product.objects.filter(order__order_date__gte=year_ago).distinct()

    # Рендерим шаблон и передаем списки товаров
    return render(request, 'product_list.html', {
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products
    })
# Create your views here.
