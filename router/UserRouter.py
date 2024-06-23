from fastapi import APIRouter

from controller.UserController import UserController
from model.schemas import UserSchema

router_user = APIRouter()
users = UserController()


@router_user.get("/user/{id}")
def get_user(id: int):
    return users.get(id)


@router_user.post("/user/")
def add_user(user_data: UserSchema):
    return users.add(user_data)


@router_user.put("/user/{id}")
def update_user(id: int, user_data: UserSchema):
    return users.update(id, user_data)


@router_user.delete("/user/{id}")
def delete_user(id: int):
    return users.delete(id)
