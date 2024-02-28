import datetime
from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: Optional[int]
    name: str
    limit: float