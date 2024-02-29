from datetime import date
from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    id: Optional[int]
    date: date
    description: str
    amount: float
    account: int
    category: int
    subcategory: int
    payment_method: int