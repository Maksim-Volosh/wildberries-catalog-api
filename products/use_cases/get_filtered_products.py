from core.interfaces import ICache, IProductRepository
from products.services.cache_key_maker import make_cache_key


class GetFilteredProductsUseCase:
    def __init__(self, repo: IProductRepository, cache: ICache):
        self.repo = repo
        self.cache = cache
        
    def execute(self, request):
        cache_key = make_cache_key(request)
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        data = self.repo.get_filtered(request)
        if data:
            self.cache.set(cache_key, data, 60*5)
        return data
    