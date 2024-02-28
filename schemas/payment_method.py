from pydantic import BaseModel
from typing import Optional

class Payment_method(BaseModel):
    id: Optional[int]
    name: str