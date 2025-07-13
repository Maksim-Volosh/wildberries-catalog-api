from abc import ABC, abstractmethod
from typing import Any, Literal


class IProductRepository(ABC):
    @abstractmethod
    def create_or_update(self, products: list[dict]) -> Literal[True]:
        ...
        
    @abstractmethod
    def get_filtered(self, request) -> Any:
        ...