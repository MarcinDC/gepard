from django.urls import path
from .views import all_products, all_sellers


urlpatterns = [
    path('products/', all_products, name='all_products'),
    path('sellers/', all_sellers, name='all_sellers')
]
