import datetime
from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    id: Optional[int]
    date: datetime
    description: str
    amount: float
    account_id: int
    category_id: int
    sub_category_id: int
    payment_method_id: int