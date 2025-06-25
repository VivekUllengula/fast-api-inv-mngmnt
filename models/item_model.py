from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    id: str
    name: str
    description: str
    price: float
    created_at: datetime