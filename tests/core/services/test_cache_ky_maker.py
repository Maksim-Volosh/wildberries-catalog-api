import unittest
from core.services.build_cache_key import build_cache_key


class TestBuildCacheKey(unittest.TestCase):

    def test_with_params(self):
        params = {
            'min_price': '100',
            'max_price': '500',
            'name': 'laptop'
        }
        key = build_cache_key(params)
        self.assertTrue(key.startswith('products:'))
        self.assertEqual(len(key), len('products:') + 32)  # md5 hash

    def test_empty_params(self):
        params = {}
        key = build_cache_key(params)
        self.assertEqual(key, 'products:base')

    def test_same_params_order_does_not_matter(self):
        params1 = {
            'min_price': '100',
            'max_price': '500'
        }
        params2 = {
            'max_price': '500',
            'min_price': '100'
        }
        key1 = build_cache_key(params1)
        key2 = build_cache_key(params2)
        self.assertEqual(key1, key2)

    def test_different_params_give_different_keys(self):
        params1 = {'min_price': '100'}
        params2 = {'min_price': '200'}
        key1 = build_cache_key(params1)
        key2 = build_cache_key(params2)
        self.assertNotEqual(key1, key2)
