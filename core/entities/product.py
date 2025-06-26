from dataclasses import dataclass

@dataclass
class ParsedProduct:
    id: int
    name: str
    rating: float
    feedbacks: int
    basic_price: int
    discount_price: int
    wb_wallet_price: int
    
