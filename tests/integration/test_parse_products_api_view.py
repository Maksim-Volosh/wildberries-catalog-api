from unittest.mock import patch

import pytest
from django.core.cache import cache
from rest_framework.test import APIClient

from products.models import Product


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()

@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()

@pytest.fixture(autouse=True)
def mock_wb_parser():
    fake_products = [
        {
            "id": 1, "name": "Mock Keyboard", "rating": 4.5,
            "feedbacks": 10, "basic_price": 1000,
            "discount_price": 800, "wb_wallet_price": 784,
        },
        {
            "id": 2, "name": "Mock Mouse", "rating": 5.0,
            "feedbacks": 5, "basic_price": 500,
            "discount_price": 400, "wb_wallet_price": 392,
        },
    ]
    with patch("infrastructure.parsers.wildberries.wildberries_parser.get_products", return_value=fake_products):
        yield 

@pytest.mark.django_db
def test_without_query(api_client):
    response = api_client.post("/api/v1/parse_products/")
    assert response.status_code == 400
    assert response.data == {"query": ["This field is required."]}
    
@pytest.mark.django_db
def test_invalid_pages(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 0})
    assert response.status_code == 400

    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": -5})
    assert response.status_code == 400
    
@pytest.mark.django_db
def test_product_fields(api_client):
    response =api_client.post("/api/v1/parse_products/", data={"query": "Keyboard"})
    assert response.status_code == 201
    product: Product | None = Product.objects.first()
    if product:
        assert product.name is not None
        assert product.discount_price > 0
    
@pytest.mark.django_db
def test_with_query(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard"})
    assert response.status_code == 201
    assert Product.objects.count() > 1
    assert response.data == {"message":"Products parsed and created successfully"}
    
@pytest.mark.django_db
def test_with_query_and_pages(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 2})
    assert response.status_code == 201
    assert Product.objects.count() > 1
    assert response.data == {"message":"Products parsed and created successfully"}
    
    
    
