import math

import requests

from core.exceptions import NoAccessToWildberriesAPI
from core.interfaces.parser import IProductParser


class WildberriesParser(IProductParser):
    def __init__(self, url):
        self.url = url
        
    def get_products(self, query: str, pages: int) -> list[dict] | list:
        products = []
        for page in range(1, pages + 1):
            response = self._response(query, page)
            if response.status_code != 200:
                raise NoAccessToWildberriesAPI(
                    f"Wildberries API returned invalid response: {response.status_code} {response.reason}"
                )
            
            data = response.json()
            parsed_products: list[dict] = self._parse_products(data)
            products.extend(parsed_products)

        return products
    
    def _response(self, query: str, page: int):
        response = requests.get(f"{self.url}&query={query}&page={page}")
        return response
    
    def _parse_products(self, data)-> list[dict]:
        products = []
        products_data = data.get("data", {}).get("products", [])
        if products_data:
            for product in products_data:
                id = product.get("id", {})
                name = product.get("name", {})
                rating = product.get("reviewRating", {})
                feedbacks = product.get("feedbacks", {})
                basic_price = product.get("sizes", [])[0].get("price", {}).get("basic", {})
                discount_price = product.get("sizes", [])[0].get("price", {}).get("product", {})
                
                normalized_basic_price = self._normalize_price(basic_price)
                normalized_discount_price = self._normalize_price(discount_price)
                wb_wallet_price = self._count_wb_wallet_price(normalized_discount_price)
                
                products.append({
                    "id": id,
                    "name": name,
                    "rating": rating,
                    "feedbacks": feedbacks,
                    "basic_price": normalized_basic_price,
                    "discount_price": normalized_discount_price,
                    "wb_wallet_price": wb_wallet_price,
                })
        return products
    
    def _normalize_price(self, price: int) -> int:
        return price // 100
    
    def _count_wb_wallet_price(self, normalized_discount_price: int) -> int:
        return math.floor(normalized_discount_price - normalized_discount_price * 0.02 + 0.5)
    

            

wildberries_parser = WildberriesParser("https://search.wb.ru/exactmatch/ru/common/v13/search?dest=-1257786&lang=ru&resultset=catalog&sort=popular")


# Usage:
# data = wildberries_parser.get_products("тапочки", 3)
# print(data)