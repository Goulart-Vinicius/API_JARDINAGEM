import peewee

db = peewee.SqliteDatabase('./banco.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
