from django.core.cache import cache

from core.interfaces.cache import ICache

class DjangoCache(ICache):
    def get(self, key: str):
        return cache.get(key)

    def set(self, key: str, value, timeout=None):
        return cache.set(key, value, timeout=timeout)
