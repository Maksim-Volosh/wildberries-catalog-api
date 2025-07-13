import unittest
from unittest.mock import Mock

import pytest

from core.exceptions import NotFoundByQuery, QueryIsRequired
from core.use_cases import ParseProductsUseCase


class TestParseProductsUseCase(unittest.TestCase):

    def test_with_data(self):
        data = [{'products': 1}, {'products': 2}]
        parser = Mock()
        parser.get_products.return_value = data
        repo = Mock()
        
        use_case = ParseProductsUseCase(parser, repo)
        use_case.execute(query='query', pages=1)

        parser.get_products.assert_called_once_with(query='query', pages=1)
        repo.create_or_update.assert_called_once_with(data)
        
    def test_without_data(self):
        data = []
        parser = Mock()
        parser.get_products.return_value = data
        repo = Mock()
        
        use_case = ParseProductsUseCase(parser, repo)
        with pytest.raises(NotFoundByQuery):
            use_case.execute(query='query', pages=1)

        parser.get_products.assert_called_once_with(query='query', pages=1)
        repo.create_or_update.assert_not_called()
        
    def test_without_query(self):
        parser = Mock()
        repo = Mock()
        
        use_case = ParseProductsUseCase(parser, repo)
        with pytest.raises(QueryIsRequired):
            use_case.execute(query='', pages=1)

        parser.get_products.assert_not_called()
        repo.create_or_update.assert_not_called()
        
