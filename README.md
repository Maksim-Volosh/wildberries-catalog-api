# Wildberries Catalog API

This is a Django REST framework API for working with Wildberries products using Clean Architecture (Onion Architecture). The API provides endpoints for parsing products from Wildberries by query, saving or updating products to the database, filtering products by price, rating, feedbacks and name, as well as caching products for 5 minutes.

## Features

- **Parser**: Parse products from Wildberries by query and save to database
- **Database**: Save or update products to the database with hashmap
- **Filter**: Filter products by price, rating, feedbacks and name
- **Cache**: Cache products for 5 minutes

## Stack

- **Python 3.12**: Programming language
- **Django**: Python web framework
- **Django REST framework**: Python framework for building APIs
- **Django-filter**: Python package for adding filters to Django views
- **Docker**: Containerization platform
- **Docker Compose**: Tool for defining and running multi-container Docker applications
- **PostgreSQL**: Open source relational database management system
- **Redis**: Open source, in-memory data structure store

## Installation

1. Clone repository: ```git clone https://github.com/Maksim-Volash/wildberries-catalog.git```
2. Create `.env` in root directory and set environment variables: 
    ```.env
    SECRET_KEY = "SECRET_KEY"
    DEBUG = True
    POSTGRES_DB=wildberries_db
    POSTGRES_USER=postgres_user
    POSTGRES_PASSWORD=postgres_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
3. Build and run container: ```docker-compose up --build```
4. Create superuser: ```python manage.py createsuperuser```
5. Open in browser: `http://localhost:8000/admin/`

## Endpoints

### `POST /api/v1/parse_products/`: Parse products by query for pages and save to database
#### Example:
  - Request body:
    ```json
    {
        "query": "query",
        "pages": 1
    }
    ```
  - Response `201 Created`:
    ```json
    {
        "message": "Products parsed and created successfully"
    }
    ```
    #
  - Request body:
    ```json
    {
    "pages": 10
    }
    ```
  - Response `400 Bad Request`:
    ```json
    {
        "query": [
            "This field is required."
        ]
    }
    ```
    #
  - Request body:
    ```json
    {
    "query": "sdfjsdhfjsdhjfhgdssdjgfdsf",
    "pages": 1
    }
    ```
  - Response `404 Not Found`:
    ```json
    {
        "error": "Products not found by query"
    }
    ```

### `GET /api/v1/products/`: Get products by filters:
  - `?name=<name>`: Get products by name
  - `?min_price=100`: Get products by min price
  - `?max_price=1000`: Get products by max price
  - `?min_rating=3`: Get products by min rating
  - `?max_rating=4`: Get products by max rating
  - `?min_feedbacks=50`: Get products by min feedbacks
  - `?max_feedbacks=100`: Get products by max feedbacks

#### Example:
- Request `GET /api/v1/products/?name=shirt&min_price=100&max_price=1000&min_rating=3&max_rating=4`:
    
- Response `200 OK`:
    ```json
    [
        {
            "id": 233300690,
            "name": "Футболка Gym T-Shirt",
            "rating": 3.8,
            "feedbacks": 4,
            "basic_price": 6990,
            "discount_price": 3522,
            "wb_wallet_price": 3452
        },
        {
            "id": 12497158,
            "name": "Футболка L. SS T-SHIRT BE ONE",
            "rating": 3.8,
            "feedbacks": 9,
            "basic_price": 3490,
            "discount_price": 1256,
            "wb_wallet_price": 1231
        }
    ]
    ```
#
- Request `GET /api/v1/products/?name=djhfkdshfkj&min_price=100`:

- Response `404 Not Found`:
    ```json
    {
        "error": "Products not found"
    }
    ```

## Models

- `Product`: id, name, rating, feedbacks, basic_price, discount_price, wb_wallet_price

## Serializers

- `ParseProductInputSerializer`: query, pages
- `ProductSerializer`: id, name, rating, feedbacks, basic_price, discount_price, wb_wallet_price

## Use cases

- `GetFilteredProductsUseCase`: Get products by query and filters
- `ProductParserUseCase`: Parse products from Wildberries API and save to database

## Exceptions

- `QueryIsRequired`: Query param is required
- `NotFoundByQuery`: Products not found by query


