from core.interfaces import ICache, IProductRepository
from typing import Callable

class FilterProductsUseCase:
    def __init__(
        self,
        repo: IProductRepository,
        cache: ICache,
        build_cache_key: Callable[[dict], str]
    ):
        self.repo = repo
        self.cache = cache
        self.build_cache_key = build_cache_key
        
    def execute(self, filtered_params: dict) -> list:
        cache_key = self.build_cache_key(filtered_params)
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        data = self.repo.get_filtered(filtered_params)
        if data:
            self.cache.set(cache_key, data, 60*5)
        return data
    