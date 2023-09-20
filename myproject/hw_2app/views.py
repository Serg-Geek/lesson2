from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Product
from .forms import ProductForm

def product_list(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    current_date = timezone.now()
    week_ago = current_date - timedelta(days=7)
    month_ago = current_date - timedelta(days=30)
    year_ago = current_date - timedelta(days=365)

    week_products = Product.objects.filter(order__order_date__gte=week_ago).distinct()
    month_products = Product.objects.filter(order__order_date__gte=month_ago).distinct()
    year_products = Product.objects.filter(order__order_date__gte=year_ago).distinct()

    return render(request, 'product_list.html', {
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products,
        'form': form,
    })
