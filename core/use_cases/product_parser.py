from typing import Literal

from core.interfaces import IProductParser, IProductRepository
from core.exceptions import NotFoundByQuery, QueryIsRequired


class ParseProductsUseCase:
    def __init__(self, parser: IProductParser, repo: IProductRepository):
        self.parser = parser
        self.repo = repo
        
    def execute(self, query: str, pages: int = 1) -> None:
        if not query:
            raise QueryIsRequired("Query param is required")
        products = self.parser.get_products(query=query, pages=pages)
        if products:
            self.repo.create_or_update(products)
        else:
            raise NotFoundByQuery("Products not found by query")

