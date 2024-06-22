from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = 'client'

    class Config:
        from_attributes = True


class ServicesSchema(BaseModel):
    name: str
    price: float
    time: str

    class Config:
        from_attributes = True
