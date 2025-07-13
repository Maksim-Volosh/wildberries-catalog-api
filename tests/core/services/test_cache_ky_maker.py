import unittest
from unittest.mock import Mock
from core.services import make_cache_key


class TestMakeCacheKey(unittest.TestCase):

    def test_make_cache_key_with_allowed_filters(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'min_price=100&max_price=500&name=laptop'
        }
        key = make_cache_key(mock_request)
        self.assertTrue(key.startswith('products:'))
        self.assertEqual(len(key), len('products:') + 32)  # md5 — это 32 символа

    def test_make_cache_key_with_disallowed_filters(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'foo=bar&baz=qux'
        }
        key = make_cache_key(mock_request)
        self.assertEqual(key, 'products:base')

    def test_make_cache_key_mixed_filters(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'foo=bar&min_price=300&max_rating=5'
        }
        key = make_cache_key(mock_request)
        self.assertTrue(key.startswith('products:'))

    def test_make_cache_key_empty_query(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': ''
        }
        key = make_cache_key(mock_request)
        self.assertEqual(key, 'products:base')

