from abc import ABC, abstractmethod


class IParserProducts(ABC):
    @abstractmethod
    def get_products(self, query: str, pages: int) -> list[dict] | list:
        pass