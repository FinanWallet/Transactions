from datetime import date
from pydantic import BaseModel

class RecordIn(BaseModel):
    user_id: int
    account_id: int    
    category_id: int
    subcategory_id: int
    type: bool
    date: date
    amount: float
    description: str

class RecordOut(BaseModel):
    id: int
    user_id: int
    account_id: int    
    category_id: int
    subcategory_id: int
    type: bool
    date: date
    amount: float
    description: str