from abc import ABC, abstractmethod
from typing import Literal


class IProductRepository(ABC):
    @abstractmethod
    def create_products(self, products) -> Literal[True]:
        ...