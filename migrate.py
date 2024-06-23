from model.DataBase import db
from model.RequestModel import Request
from model.ServicesModel import Services
from model.UserModel import User


def create_tables():
    with db:
        print("Connecting to database...")
        with db:
            db.create_tables([User, Services, Request], safe=True)
        print("Tables created.")


if __name__ == '__main__':
    create_tables()
