from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('code', 'name', 'desc')
    list_filter = ('name',)
    search_fields = ('code', 'name', 'desc')

