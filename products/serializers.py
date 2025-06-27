from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        

class ParseProductInputSerializer(serializers.Serializer):
    query = serializers.CharField(required=True)
    pages = serializers.IntegerField(required=False, default=1, min_value=1)
