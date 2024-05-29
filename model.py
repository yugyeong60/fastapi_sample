from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id: int = 0
    item: str
    author: str
    timestamp: datetime = None