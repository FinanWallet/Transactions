from datetime import date
from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    user_id: int
    account_id: int    
    category_id: int
    subcategory_id: int
    type: bool
    date: date
    amount: float
    description: str