from fastapi import APIRouter

from controller.ServicesController import ServicesController
from model.schemas import ServicesSchema

router_services = APIRouter()
services = ServicesController()

@router_services.get("/services/")
def index():
    return services.get_all()


@router_services.get("/services/{id}")
def get_user(id: int):
    return services.get(id)


@router_services.post("/services/")
def add_user(services_data: ServicesSchema):
    return services.add(services_data)


@router_services.put("/services/{id}")
def update_user(id: int, services_data: ServicesSchema):
    return services.update(id, services_data)


@router_services.delete("/services/{id}")
def delete_user(id: int):
    return services.delete(id)
