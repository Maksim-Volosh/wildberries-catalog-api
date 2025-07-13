from adapters import extract_allowed_filters
from core.services import build_cache_key
from core.use_cases import FilterProductsUseCase, ParseProductsUseCase
from infrastructure import DjangoCache, ORMProductRepository, wildberries_parser


class ProductContainer:
    def __init__(self):
        self.repo = ORMProductRepository()
        self.cache = DjangoCache()
        self.build_cache_key = build_cache_key
        self.parser = wildberries_parser

    def get_filter_products_use_case(self):
        return FilterProductsUseCase(
            repo=self.repo,
            cache=self.cache,
            build_cache_key=self.build_cache_key
        )

    def get_parse_products_use_case(self):
        return ParseProductsUseCase(
            parser=self.parser,
            repo=self.repo
        )
        
    def get_extract_allowed_filters(self):
        return extract_allowed_filters
