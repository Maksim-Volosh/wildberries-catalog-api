import pytest
from django.core.cache import cache
from rest_framework.test import APIClient

from products.models import Product


@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()

@pytest.fixture
def api_client() -> APIClient:
    return APIClient()

@pytest.fixture
def create_products():
    Product.objects.create(
        name="Keyboard",
        rating=3.3,
        feedbacks=100,
        basic_price=1000,
        discount_price=897,
        wb_wallet_price=800,
    )
    Product.objects.create(
        name="Mouse",
        rating=5,
        feedbacks=10,
        basic_price=500,
        discount_price=479,
        wb_wallet_price=450,
    )

@pytest.mark.django_db
def test_products_list_empty(api_client):
    response = api_client.get("/api/v1/products/")
    assert response.data == {"error": "Products not found"}
    assert response.status_code == 404

@pytest.mark.django_db
def test_filter_by_name_not_found(api_client, create_products):
    response = api_client.get("/api/v1/products/?name=Nonexistent")
    assert response.status_code == 404
    assert response.data == {"error": "Products not found"}


@pytest.mark.django_db
def test_products_list(api_client, create_products):
    response = api_client.get("/api/v1/products/")
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_filter_by_name(api_client, create_products):
    response = api_client.get("/api/v1/products/?name=Mouse")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Mouse"

@pytest.mark.django_db
def test_filter_by_price_range(api_client, create_products):
    response = api_client.get("/api/v1/products/?min_price=500&max_price=1000")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Keyboard"
    assert 500 <= response.data[0]["discount_price"] <= 1000

@pytest.mark.django_db
def test_filter_by_rating(api_client, create_products):
    response = api_client.get("/api/v1/products/?min_rating=4&max_rating=5")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Mouse"
    assert 4 <= response.data[0]["rating"] <= 5

@pytest.mark.django_db
def test_filter_by_feedbacks(api_client, create_products):
    response = api_client.get("/api/v1/products/?min_feedbacks=15&max_feedbacks=200")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Keyboard"
    assert 15 <= response.data[0]["feedbacks"] <= 200

@pytest.mark.django_db
def test_filter_by_name_and_price(api_client, create_products):
    response = api_client.get("/api/v1/products/?name=Keyboard&min_price=800")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Keyboard"

    response = api_client.get("/api/v1/products/?name=Keyboard&min_price=2000")
    assert response.status_code == 404
    assert response.data == {"error": "Products not found"}

@pytest.mark.django_db
def test_filter_by_rating_edge(api_client, create_products):
    response = api_client.get("/api/v1/products/?min_rating=5")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Mouse"
