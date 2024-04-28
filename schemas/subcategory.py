from pydantic import BaseModel
from typing import Optional

class Subcategory(BaseModel):
    id: int
    name: str
    category_id: int