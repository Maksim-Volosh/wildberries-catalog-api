from abc import ABC, abstractmethod


class ICache(ABC):
    @abstractmethod
    def get(self, key: str):
        ...
        
    @abstractmethod
    def set(self, key: str, value, timeout=None):
        ...