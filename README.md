# 🛍️ Wildberries Catalog API

[![Abblix OIDC Server](https://i.imgur.com/BESSBGm.png)](https://github.com/Maksim-Volosh/wildberries-catalog-api)


[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.x-red?logo=django)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker--Compose-ready-blue?logo=docker)](https://docs.docker.com/compose/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7.2-red?logo=redis)](https://redis.io/)
[![Pytest](https://img.shields.io/badge/Pytest-tested-brightgreen?logo=pytest)](https://docs.pytest.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Clean--Architecture-yellowgreen)](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
[![License](https://img.shields.io/github/license/Maksim-Volosh/wildberries-catalog-api)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Maksim-Volosh/wildberries-catalog-api?color=purple)](https://github.com/Maksim-Volosh/wildberries-catalog-api/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/Maksim-Volosh/wildberries-catalog-api)](https://github.com/Maksim-Volosh/wildberries-catalog-api)
[![Open Issues](https://img.shields.io/github/issues/Maksim-Volosh/wildberries-catalog-api?label=issues)](https://github.com/Maksim-Volosh/wildberries-catalog-api/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/Maksim-Volosh/wildberries-catalog-api/pulls)
[![Made with ❤️by Maksim](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)](https://github.com/Maksim-Volosh)

⭐ Star us on GitHub — it motivates us a lot!

[![Share on X](https://img.shields.io/badge/share-000000?logo=x&logoColor=white)](https://x.com/intent/tweet?text=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Maksim-Volosh/wildberries-catalog-api%20%23Django%20%23API%20%23CleanArchitecture)
[![Share on Facebook](https://img.shields.io/badge/share-1877F2?logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/Maksim-Volosh/wildberries-catalog-api)
[![Share on LinkedIn](https://img.shields.io/badge/share-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Maksim-Volosh/wildberries-catalog-api)
[![Share on Reddit](https://img.shields.io/badge/share-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/submit?title=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Maksim-Volosh/wildberries-catalog-api)
[![Share on Telegram](https://img.shields.io/badge/share-0088CC?logo=telegram&logoColor=white)](https://t.me/share/url?url=https://github.com/Maksim-Volosh/wildberries-catalog-api&text=Check%20out%20this%20project%20on%20GitHub)



## 📚 Table of Contents

- [🎓 About](#-about)
- [📌 Features](#-features)
- [🧱 Tech Stack](#-tech-stack)
- [🚀 Installation](#-installation)
- [🎯 Endpoints](#-endpoints)
  - [POST /api/v1/parse_products/](#post-apiv1parse_products-parse-products-by-query-for-pages-and-save-to-database)
  - [GET /api/v1/products/](#get-apiv1products-get-products-by-filters)
- [🧩 Models](#models)
- [📦 Serializers](#serializers)
- [🧠 Use Cases](#use-cases)
- [⚠️ Exceptions](#exceptions)
- [✅ Testing](#testing)

## 🎓 About

This is a Django REST framework API for working with Wildberries products using Clean Architecture (Onion Architecture). The API provides endpoints for parsing products from Wildberries by query, saving or updating products to the database, filtering products by price, rating, feedbacks and name, as well as caching products for 5 minutes.

## 📌 Features

- **Parser**: Parse products from Wildberries by query and save to database
- **Database**: Save or update products to the database with hashmap
- **Filter**: Filter products by price, rating, feedbacks and name
- **Cache**: Cache products for 5 minutes
- **Testing**: Unit tests for services and use cases

## 🧱 Tech Stack

| Technology         | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| 🐍 Python 3.12      | General-purpose programming language                                        |
| 🌿 Django           | High-level Python web framework for rapid development                      |
| 🚦 Django REST Framework | Toolkit for building Web APIs with Django                          |
| 🔍 Django-filter    | App to add filtering support to Django REST Framework                      |
| 🐳 Docker           | Platform for containerizing and deploying applications                     |
| 🧩 Docker Compose   | Tool for defining and running multi-container Docker applications           |
| 🐘 PostgreSQL       | Advanced open-source relational database system                             |
| 🔴 Redis            | In-memory key-value store used for caching                                 |
| 🧪 Pytest           | Framework for writing simple and scalable test cases in Python             |


## 🚀 Installation

1. 🔁 Clone repository: ```git clone https://github.com/Maksim-Volash/wildberries-catalog.git```
2. 📄 Create `.env` in root directory and set environment variables: 
      ```.env
      SECRET_KEY = "SECRET_KEY"
      DEBUG = True
      POSTGRES_DB=wildberries_db
      POSTGRES_USER=postgres_user
      POSTGRES_PASSWORD=postgres_password
      POSTGRES_HOST=db
      POSTGRES_PORT=5432
      ```
3. 🐳 Build and run container: ```docker-compose up --build```
4. 🔁 Find container name: ```docker ps```:
     ```
     CONTAINER ID   IMAGE          COMMAND       NAMES
     abcd1234ef56   myapp-image    "uvicorn ..." my_running_container
     ```
5. 🧪 Run pytest by container name:
     ```docker exec -it my_running_container pytest -v```
6. 👤 Create superuser in docker by container name:
     ```docker exec -it wildberries-catalog-api_web_1 python3 manage.py createsuperuser```
7. 🌍 Open in browser: `http://localhost:8000/admin/`

## 🎯 Endpoints

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

- `FilterProductsUseCase`: Get products by query and filters
- `ParseProductsUseCase`: Parse products from Wildberries API and save to database

## Exceptions

- `QueryIsRequired`: Query param is required
- `NotFoundByQuery`: Products not found by query

## Testing

- Run unit tests: ```pytest```

