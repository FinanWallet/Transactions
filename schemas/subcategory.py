import datetime
from pydantic import BaseModel
from typing import Optional

class Subcategory(BaseModel):
    id: Optional[int]
    name: str
    account: int
    category: int