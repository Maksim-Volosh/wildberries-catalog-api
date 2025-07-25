import unittest
from unittest.mock import Mock

from core.use_cases import FilterProductsUseCase


class TestFilterProductsUseCase(unittest.TestCase):

    def test_with_data(self):
        cache = Mock()
        cache.get.return_value = [{'products': 1}, {'products': 2}]
        repo = Mock()
        build_cache_key = Mock()
        build_cache_key.return_value = 'test_key'
        
        use_case = FilterProductsUseCase(repo, cache, build_cache_key)
        result = use_case.execute(Mock())

        self.assertEqual(result, [{'products': 1}, {'products': 2}])
        cache.get.assert_called_once_with(build_cache_key.return_value)
        repo.get_filtered.assert_not_called()
        cache.set.assert_not_called()
        
    def test_without_data(self):
        cache = Mock()
        cache.get.return_value = []
        repo = Mock()
        repo.get_filtered.return_value = [{'products': 1}, {'products': 2}]
        build_cache_key = Mock()
        build_cache_key.return_value = 'test_key'
        request = Mock()
        
        use_case = FilterProductsUseCase(repo, cache, build_cache_key)
        result = use_case.execute(request)

        self.assertEqual(result, [{'products': 1}, {'products': 2}])
        cache.get.assert_called_once_with(build_cache_key.return_value)
        repo.get_filtered.assert_called_once_with(request)
        cache.set.assert_called_once_with(build_cache_key.return_value, [{'products': 1}, {'products': 2}], 300)
        