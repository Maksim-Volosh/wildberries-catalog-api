import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='discount_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='discount_price', lookup_expr='lte')
    min_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    min_feedbacks = django_filters.NumberFilter(field_name='feedbacks', lookup_expr='gte')
    max_feedbacks = django_filters.NumberFilter(field_name='feedbacks', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = []
