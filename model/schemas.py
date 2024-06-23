import time
from typing import Optional, Union

from pydantic import BaseModel, field_validator

from model.UserModel import User


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
    time: time
    user: Union[User | int]

    @field_validator('user', mode='before')
    def validate_user(cls, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
