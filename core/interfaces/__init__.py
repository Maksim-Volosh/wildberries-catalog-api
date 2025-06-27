__all__ = [
    "IParserProducts",
    "IProductRepository",
    "ICache",
]
from .cache import ICache
from .parser import IParserProducts
from .product_repository import IProductRepository