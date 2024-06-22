from model.DataBase import BaseModel, db
from model.UserModel import User
from model.ServicesModel import Services

def create_tables():
    with db:
        print("Connecting to database...")
        with db:
            db.create_tables([User, Services], safe=True)
        print("Tables created.")


if __name__ == '__main__':
    create_tables()