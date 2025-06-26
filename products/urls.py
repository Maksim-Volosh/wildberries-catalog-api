from django.urls import path
from .views import ProductListAPIView, ProductsView

urlpatterns = [
    path('parse_products/', ProductsView.as_view(), name='parse_products'),
    path('products/', ProductListAPIView.as_view(), name='products'),
]
