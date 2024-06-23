from peewee import *

from model.DataBase import BaseModel
from model.ServicesModel import Services
from model.UserModel import User


class Request(BaseModel):
    client = ForeignKeyField(User)
    date = DateTimeField()
    service = ForeignKeyField(Services)
    Gardner = ForeignKeyField(User)
    active = BooleanField(default=True)
