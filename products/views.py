from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.using('products_db').all()
    return render(request, 'product_list.html', {'products': products})