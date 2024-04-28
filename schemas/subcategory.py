from pydantic import BaseModel

class SubcategoryIn(BaseModel):
    name: str
    category_id: int

class SubcategoryOut(BaseModel):
    id: int
    name: str
    category_id: int