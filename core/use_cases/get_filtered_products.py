from core.interfaces import ICache, IProductRepository


class FilterProductsUseCase:
    def __init__(self, repo: IProductRepository, cache: ICache, cache_key_maker):
        self.repo = repo
        self.cache = cache
        self.cache_key_maker = cache_key_maker
        
    def execute(self, request):
        cache_key = self.cache_key_maker(request)
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        data = self.repo.get_filtered(request)
        if data:
            self.cache.set(cache_key, data, 60*5)
        return data
    