from django.urls import path

from .views import ParseProductsView, ProductListAPIView

urlpatterns = [
    path('parse_products/', ParseProductsView.as_view(), name='parse_products'),
    path('products/', ProductListAPIView.as_view(), name='products'),
]
