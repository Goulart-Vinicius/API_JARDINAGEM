import datetime
import time
from typing import Optional, Union

from pydantic import BaseModel, field_validator

from model.ServicesModel import Services
from model.UserModel import User


class UserSchema(BaseModel):
    id: Optional[Union[int | str]] = None
    name: str
    email: str
    password: str
    role: Optional[str] = 'client'

    class Config:
        from_attributes = True


class ServicesSchema(BaseModel):
    id: Optional[Union[int | str]] = None
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


class DateTime:
    pass


class RequestSchema(BaseModel):
    id: Optional[Union[int | str]] = None
    client: Union[User | int]
    date: Union[str | DateTime]
    service: Union[Services | int]
    gardner: Union[User | int]

    @field_validator('gardner', mode='before')
    def validate_user(cls, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    @field_validator('service', mode='before')
    def validate_user(cls, v):
        if isinstance(v, ServicesSchema):
            return v.id
        return v

    @field_validator('client', mode='before')
    def validate_user(cls, v):
        if isinstance(v, UserSchema):
            return v.id
        return v

    @field_validator('date', mode='before')
    def validate_date(cls, v):
        if isinstance(v, int):
            return datetime.datetime.fromtimestamp(v / 1000).strftime('%d/%m/%y')
        elif isinstance(v, datetime.datetime):
            return v.strftime('%d/%m/%y')
        elif isinstance(v, str):
            try:
                datetime.datetime.strptime(v, '%d/%m/%y')
                return v
            except ValueError:
                try:
                    datetime.datetime.strptime(v, '%d/%m/%Y')
                    return v
                except ValueError:
                    raise ValueError("Input should be a valid date in DD/MM/YY or DD/MM/YYYY format")
        raise ValueError("Input should be a valid date format")

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
