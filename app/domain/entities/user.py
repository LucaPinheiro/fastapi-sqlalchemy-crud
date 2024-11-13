from typing import Optional
from pydantic import BaseModel

class UserEntity(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str
