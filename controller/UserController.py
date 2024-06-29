from fastapi import HTTPException

from model.UserModel import User
from model.schemas import UserSchema


class UserController:
    def __init__(self):
        self.UserModel = User()

    def get(self, user_id: int):
        try:
            user = self.UserModel.get_by_id(user_id)
            if user.active is False:
                raise
            return UserSchema.model_validate(user).model_dump()
        except:
            raise HTTPException(status_code=404, detail="User not found")

    def add(self, user_data: UserSchema):
        try:
            user_data = user_data.model_dump()
            user_post = self.UserModel.create(**user_data)
            return UserSchema.model_validate(user_post).model_dump()

        except Exception as e:
            if str(e) == 'UNIQUE constraint failed: user.email':
                raise HTTPException(status_code=409, detail="Email already exists")
            else:
                raise HTTPException(status_code=500, detail=str(e))

    def update(self, user_id: int, user_data: UserSchema):
        try:
            user_data = user_data.model_dump()
            user = self.UserModel.get_by_id(user_id)
            query = self.UserModel.update(**user_data).where(User.id == user_id)
            query.execute()
            return self.get(user_id)
        except Exception as e:

            if str(e) == 'UNIQUE constraint failed: user.email':
                raise HTTPException(status_code=409, detail="Email already exists")
            else:
                raise HTTPException(status_code=500, detail=str(e))

    def delete(self, user_id):
        try:
            user = self.UserModel.get_by_id(user_id)

            user.active = False
            user.save()

            return {"message": "User deactivated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
