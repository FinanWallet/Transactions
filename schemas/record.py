import datetime
from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    id: Optional[int]
    date: datetime
    description: str
    amount: float
    account: int
    category: int
    subcategory: int
    payment_method: int