from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: optional[int]
    name: str