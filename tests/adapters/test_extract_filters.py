import unittest
from unittest.mock import Mock
from adapters import extract_allowed_filters


class TestExtractAllowedFilters(unittest.TestCase):

    def test_order_with_valid_params(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'max_price=500&name=laptop&min_price=100&'
        }
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {
            'min_price': '100',
            'max_price': '500',
            'name': 'laptop'
        })

    def test_with_disallowed_params(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'foo=bar&baz=qux'
        }
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {})
        
    def test_order_with_mixed_params(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'foo=bar&baz=qux&name=laptop&max_price=500'
        }
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {
            'max_price': '500',
            'name': 'laptop'
        })

    def test_mixed_params(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': 'foo=bar&min_price=300&max_rating=5'
        }
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {
            'min_price': '300',
            'max_rating': '5'
        })

    def test_empty_query(self):
        mock_request = Mock()
        mock_request.META = {
            'QUERY_STRING': ''
        }
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {})

    def test_missing_query_string(self):
        mock_request = Mock()
        mock_request.META = {}
        result = extract_allowed_filters(mock_request)
        self.assertEqual(result, {})


