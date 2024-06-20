from peewee import *
from model.DataBase import BaseModel, db

roles = ('admin', 'functionary', 'client')


class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField(choices=roles, default='client')

