from django.urls import path

from .views import ParseProductsAPIView, ProductListAPIView

urlpatterns = [
    path('parse_products/', ParseProductsAPIView.as_view(), name='parse_products'),
    path('products/', ProductListAPIView.as_view(), name='products'),
]
