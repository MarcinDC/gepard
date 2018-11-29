from django.shortcuts import render
from .models import Product, Seller

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


def all_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'all_sellers.html', {'sellers': sellers})
