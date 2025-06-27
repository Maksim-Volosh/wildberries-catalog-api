from typing import Literal

from core.interfaces.product import IProductRepository
from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductSerializer


class ORMProductRepository(IProductRepository):
    def create_or_update_products(self, products: list[dict]) -> Literal[True]:
        product_ids = [pr["id"] for pr in products]
        
        existing_products = Product.objects.filter(id__in=product_ids)
        existing_hashmap = {pr.id: pr for pr in existing_products} # type: ignore
        
        to_create = []
        to_update = []
        
        for data in products:
            product_id = data["id"]
            if product_id in existing_hashmap:
                obj = existing_hashmap[product_id]
                
                obj.name = data["name"]
                obj.rating = data["rating"]
                obj.feedbacks = data["feedbacks"]
                obj.basic_price = data["basic_price"]
                obj.discount_price = data["discount_price"]
                obj.wb_wallet_price = data["wb_wallet_price"]
                
                to_update.append(obj)
            else:
                to_create.append(Product(**data))
                
        if to_create:
            Product.objects.bulk_create(to_create)
            
        if to_update:
            Product.objects.bulk_update(
                to_update,
                ["name", "rating", "feedbacks", "basic_price", "discount_price", "wb_wallet_price"]
            )
            
        return True
    
    def get_filtered(self, request):
        queryset = Product.objects.all()
        filtered_qs = ProductFilter(request.GET, queryset=queryset).qs
        return ProductSerializer(filtered_qs, many=True).data
