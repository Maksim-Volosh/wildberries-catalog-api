from typing import Literal
from core.interfaces.parser import IParserProducts
from core.interfaces.product import IProductRepository
from products.models import Product


class ORMProductRepository(IProductRepository):
    def create_products(self, products) -> Literal[True]:
        Product.objects.bulk_create([Product(**product) for product in products], ignore_conflicts=True)
        return True
    
