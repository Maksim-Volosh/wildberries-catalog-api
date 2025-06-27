from typing import Literal

from core.interfaces import IParserProducts, IProductRepository
from core.exceptions import NotFoundByQuery, QueryIsRequired


class ParseProductsUseCase:
    def __init__(self, parser: IParserProducts, repo: IProductRepository):
        self.parser: IParserProducts = parser
        self.repo: IProductRepository = repo
        
    def execute(self, query: str, pages: int = 1) -> None | Literal[False]:
        if not query:
            raise QueryIsRequired("Query param is required")
        products = self.parser.get_products(query=query, pages=pages)
        if products:
            self.repo.create_or_update_products(products)
        else:
            raise NotFoundByQuery("Products not found by query")

