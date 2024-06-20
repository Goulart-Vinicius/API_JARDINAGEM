from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from model.UserModel import User


class UserController:
    def __init__(self):
        self.UserModel = User()

    def get(self, user_id: int):
        try:
            data = self.UserModel.get_by_id(user_id)
            return jsonable_encoder(data)
        except Exception as error:
            raise HTTPException(status_code=401, detail="User not found")

    def add(self, user_data: dict):
        try:
            return self.UserModel.create(**user_data)

        except Exception:
            return HTTPException(status_code=409, detail="Email already exists")
