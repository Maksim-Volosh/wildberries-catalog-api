from typing import Literal

from core.interfaces.parser import IParserProducts
from core.interfaces.product import IProductRepository

from products.exceptions import QueryIsRequired, NotFoundByQuery


class ProductParserUseCase:
    def __init__(self, parser: IParserProducts, repo: IProductRepository):
        self.parser: IParserProducts = parser
        self.repo: IProductRepository = repo
        
    def execute(self, request) -> None | Literal[False]:
        query = request.query_params.get("query")
        pages = request.query_params.get("pages", 1)
        if not query:
            raise QueryIsRequired("Query param is required")
        products = self.parser.get_products(query=query, pages=pages)
        if products:
            self.repo.create_products(products)
        else:
            raise NotFoundByQuery("Products not found by query")

