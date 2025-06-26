from core.interfaces.parser import IParserProducts
from core.interfaces.product import IProductRepository

from products.exceptions import QueryIsRequired


class ProductParserUseCase:
    def __init__(self, parser: IParserProducts, repo: IProductRepository):
        self.parser: IParserProducts = parser
        self.repo: IProductRepository = repo
        
    def execute(self, request) -> None:
        query = request.query_params.get("query")
        pages = request.query_params.get("pages", 1)
        if not query:
            raise QueryIsRequired("Query param is required")
        products = self.parser.get_products(query=query, pages=pages)
        self.repo.create_products(products)

