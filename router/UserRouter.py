from fastapi import APIRouter, Request, Body
from controller.UserController import UserController

router_user = APIRouter()
users = UserController()

@router_user.get("/user/")
def home():
    return "aoba"

@router_user.get("/user/{id}")
def get_user(id: int):
    return users.get(id)

@router_user.post("/user/")
def add_user(user_data:dict = Body(...)):
    return users.add(user_data)

@router_user.put("/user/{id}")
def update_user(id:int, user_data:dict = Body(...)):
    return users.update(id, user_data)

@router_user.delete("/user/{id}")
def delete_user(id:int):
    return users.delete(id)



