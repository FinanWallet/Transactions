from datetime import date
from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    id: Optional[int]
    account_id: int    
    subcategory_id: int
    date: date
    amount: float
    description: str
    