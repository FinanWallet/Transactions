from pydantic import BaseModel
from typing import Optional

class Subcategory(BaseModel):
    name: str
    category_id: int