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

@pytest.mark.e2e
@pytest.mark.django_db
def test_without_query(api_client):
    response = api_client.post("/api/v1/parse_products/")
    assert response.status_code == 400
    assert response.data == {"query": ["This field is required."]}
    
@pytest.mark.e2e
@pytest.mark.django_db
def test_invalid_pages(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 0})
    assert response.status_code == 400

    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": -5})
    assert response.status_code == 400
    
@pytest.mark.e2e
@pytest.mark.django_db
def test_product_fields(api_client):
    response =api_client.post("/api/v1/parse_products/", data={"query": "Keyboard"})
    assert response.status_code == 201
    product: Product | None = Product.objects.first()
    if product:
        assert product.name is not None
        assert product.discount_price > 0
    
@pytest.mark.e2e
@pytest.mark.django_db
def test_with_query(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard"})
    assert response.status_code == 201
    assert Product.objects.count() > 1
    assert response.data == {"message":"Products parsed and created successfully"}

@pytest.mark.e2e
@pytest.mark.django_db
def test_with_query_and_pages(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 2})
    assert response.status_code == 201
    assert Product.objects.count() > 1
    assert response.data == {"message":"Products parsed and created successfully"}

@pytest.mark.e2e
@pytest.mark.django_db
def test_pages_affect_count(api_client):
    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 1})
    assert response.status_code == 201
    count_one_page = Product.objects.count()
    assert count_one_page > 0

    response = api_client.post("/api/v1/parse_products/", data={"query": "Keyboard", "pages": 2})
    assert response.status_code == 201
    count_two_pages = Product.objects.count()
    assert count_two_pages > count_one_page
    
    
    
