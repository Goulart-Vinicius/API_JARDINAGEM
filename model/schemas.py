import datetime
import time
from typing import Optional, Union

from pydantic import BaseModel, field_validator

from model.ServicesModel import Services
from model.UserModel import User


class UserSchema(BaseModel):
    id: int | None
    name: str
    email: str
    password: str
    role: Optional[str] = 'client'

    class Config:
        from_attributes = True


class ServicesSchema(BaseModel):
    id: int | None
    name: str
    price: float
    time: time
    user: Union[User | int]

    @field_validator('user', mode='before')
    def validate_user(self, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class DateTime:
    pass


class RequestSchema(BaseModel):
    id: int | None
    client: Union[User | int]
    date: Union[str, int]
    service: Union[Services | int]
    gardner: Union[User | int]

    @field_validator('gardner', mode='before')
    def validate_user(self, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    @field_validator('service', mode='before')
    def validate_user(self, v):
        if isinstance(v, ServicesSchema):
            return v.id
        return v

    @field_validator('client', mode='before')
    def validate_user(self, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    @field_validator('date', mode='before')
    def validate_user(self, v):
        if isinstance(v, int):
            # Convert timestamp (milliseconds) to ISO 8601 format string
            return datetime.datetime.fromtimestamp(v / 1000).isoformat()
        return v

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
