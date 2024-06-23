from peewee import *

from model.DataBase import BaseModel
from model.UserModel import User

roles = ('admin', 'functionary', 'client')


class Services(BaseModel):
    name = CharField(unique=True)
    price = FloatField()
    time = TimeField()
    active = BooleanField(default=True)
    user = ForeignKeyField(User)
