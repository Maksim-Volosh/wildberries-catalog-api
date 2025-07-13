from abc import ABC, abstractmethod


class IProductParser(ABC):
    @abstractmethod
    def get_products(self, query: str, pages: int) -> list[dict] | list:
        pass