from django.contrib import admin
from .models import Product, Seller, ProductPrice

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('code', 'name', 'desc')
    list_display = ('code', 'name', 'desc')
    list_filter = ('name',)
    search_fields = ('code', 'name', 'desc')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    fields = ('code', 'name', 'rate_count', 'stars')
    list_display = ('code', 'name', 'rate_count', 'stars')
    list_filter = ('code', 'name', 'rate_count', 'stars')
    search_fields = ('code', 'name', 'rate_count', 'stars')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    fields = ('product', 'seller', 'price', 'pricedate', 'delivery')
    list_distplay = ('product', 'seller', 'price', 'pricedate', 'delivery')
