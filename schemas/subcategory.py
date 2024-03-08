from pydantic import BaseModel
from typing import Optional

class Subcategory(BaseModel):
    id: Optional[int]
    name: str
    category_id: int