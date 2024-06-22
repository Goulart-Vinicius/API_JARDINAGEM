from peewee import *

from model.DataBase import BaseModel

roles = ('admin', 'functionary', 'client')


class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField(choices=roles, default='client')
    active = BooleanField(default=True)
