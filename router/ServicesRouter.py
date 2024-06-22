from fastapi import APIRouter, HTTPException
from controller.ServicesController import ServicesController

router_services = APIRouter()
services = ServicesController()

@router_services.get("/services/")
def index():
    return services.get_all()



'''@router_user.get("/services/{id}")
def get_user(id: int):
    return users.get(id)'''


'''@router_user.post("/user/")
def add_user(user_data: User):
    return users.add(user_data)


@router_user.put("/user/{id}")
def update_user(id: int, user_data: User):
    return users.update(id, user_data)


@router_user.delete("/user/{id}")
def delete_user(id: int):
    return users.delete(id)'''
