from core.use_cases import FilterProductsUseCase, ParseProductsUseCase
from core.services.cache_key_maker import make_cache_key
from products.infrastructure import ORMProductRepository, DjangoCache
from parsers import wildberries_parser


class ProductContainer:
    def __init__(self):
        self.repo = ORMProductRepository()
        self.cache = DjangoCache()
        self.cache_key_maker = make_cache_key
        self.parser = wildberries_parser

    def get_filter_products_use_case(self):
        return FilterProductsUseCase(
            repo=self.repo,
            cache=self.cache,
            cache_key_maker=self.cache_key_maker
        )

    def get_parse_products_use_case(self):
        return ParseProductsUseCase(
            parser=self.parser,
            repo=self.repo
        )
