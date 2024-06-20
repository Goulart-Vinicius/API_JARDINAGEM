from model.DataBase import BaseModel, db
from model.UserModel import User

def create_tables():
    with db:
        print("Connecting to database...")
        with db:
            db.create_tables([User], safe=True)
        print("Tables created.")


if __name__ == '__main__':
    create_tables()