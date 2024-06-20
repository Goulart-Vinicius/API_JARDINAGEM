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

    def update(self, user_id:int, user_data:dict):
        try:

            query = self.UserModel.update(**user_data).where(self.UserModel.id == user_id)
            query.execute()
            return self.UserModel.update()
        except Exception as e:

            if str(e) == 'UNIQUE constraint failed: user.email':
                raise HTTPException(status_code=409, detail="Email already exists")
            else:
                raise HTTPException(status_code=400, detail=str(e))

