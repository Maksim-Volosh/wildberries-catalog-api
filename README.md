# Wildberries Catalog API

This is a Django REST framework API for working with Wildberries products.

## Features

- Parse products from wildberries by query
- Filter products by price, rating, feedbacks, name
- Cache products for 5 minutes

## Installation

1. Clone repository: `git clone https://github.com/Maksim-Volash/wildberries-catalog.git`
2. Create `config.py` in root directory and set your secret key: `SECRET_KEY = 'your-secret-key'`
3. Build and run container: `docker-compose up --build`
4. Open in browser: `http://localhost:8000/api/v1/products/?query=тапочки`

## Endpoints

- `GET /api/v1/parse_products/?query=<query>&pages=<pages>`: Parse products by query for pages and save to database

- `GET /api/v1/products/`: Get products by filters
  - `name=<name>`: Get products by name
  - `name=<name>&min_price=<price>&max_price=<price>`: Get products by name and price range
  - `name=<name>&min_rating=<rating>&max_rating=<rating>`: Get products by name and rating range
  - `name=<name>&min_feedbacks=<feedbacks>&max_feedbacks=<feedbacks>`: Get products by name and feedbacks range

## Models

- `Product`: id, name, rating, feedbacks, basic_price, discount_price, wb_wallet_price

## Serializers

- `ProductSerializer`: id, name, rating, feedbacks, basic_price, discount_price, wb_wallet_price

## Use cases

- `GetFilteredProductsUseCase`: Get products by query and filters
- `ProductParserUseCase`: Parse products from Wildberries API and save to database

## Exceptions

- `QueryIsRequired`: Query param is required
- `NotFoundByQuery`: Products not found by query

