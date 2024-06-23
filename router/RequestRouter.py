from fastapi import APIRouter

from controller.RequestController import RequestController
from model.schemas import RequestSchema

router_request = APIRouter()
request = RequestController()


@router_request.get("/request/")
def index():
    return request.get_all()


@router_request.get("/request/{id}")
def get_user(id: int):
    return request.get(id)


@router_request.post("/request/")
def add_user(request_data: RequestSchema):
    return request.add(request_data)


@router_request.put("/request/{id}")
def update_user(id: int, request_data: RequestSchema):
    return request.update(id, request_data)


@router_request.delete("/request/{id}")
def delete_user(id: int):
    return request.delete(id)
