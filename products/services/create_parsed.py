from core.interfaces.parser import IParserProducts
from products.models import Product


class CreateParsedProducts:
    def __init__(self, parser: IParserProducts):
        self.parser = parser
        
    def create(self, query: str, pages: int):
        products = self.parser.get_products(query=query, pages=pages)
        
        Product.objects.bulk_create([Product(**product) for product in products], ignore_conflicts=True)
        return True
    
