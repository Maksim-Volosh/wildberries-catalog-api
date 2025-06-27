from abc import ABC, abstractmethod
from typing import Literal


class IProductRepository(ABC):
    @abstractmethod
    def create_or_update_products(self, products: list[dict]) -> Literal[True]:
        ...