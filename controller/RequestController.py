from fastapi import HTTPException

from model.RequestModel import Request
from model.schemas import RequestSchema


class RequestController:

    def __init__(self):
        self.Request = Request()

    def get_all(self):
        try:
            reuests_list = list(self.Request.select().dicts())
            request = [RequestSchema.model_validate(registro).model_dump() for registro in reuests_list]

            return request
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get(self, id_service: int):
        try:
            service = self.Services.get_by_id(id_service)

            return RequestSchema.model_validate(service).model_dump()

        except Exception as e:
            if "instance matching query does not exist" in str(e):
                raise HTTPException(status_code=404, detail='Service not found')
            HTTPException(status_code=500, detail="Internal Server Error")

    def add(self, service: RequestSchema):
        try:
            service_data = service.model_dump()
            service_model = self.Services.create(**service_data)
            service_validated = RequestSchema.model_validate(service_model)
            user = service_validated.user
            service_validated.user = user.id
            return service_validated.model_dump()
        except Exception as e:
            if 'UNIQUE constraint failed: services.name' in str(e):
                raise HTTPException(status_code=409, detail="Service already exists")
            HTTPException(status_code=500, detail='Internal Server Error')

    def update(self, service_id: int, service_data: RequestSchema):
        try:
            service_data = service_data.model_dump()
            service = self.Services.get_by_id(service_id)

            service.name = service_data['name']
            service.price = service_data['price']
            service.time = service_data['time']
            service.user = service_data['user']

            service.save()
            return RequestSchema.model_validate(self.get(service_id)).model_dump()
        except Exception as e:

            if str(e) == 'UNIQUE constraint failed: services.name':
                raise HTTPException(status_code=409, detail="Service name already exists")
            else:
                raise HTTPException(status_code=500, detail=str(e))

    def delete(self, service_id: int):
        try:
            service = self.Services.get_by_id(service_id)

            service.active = False
            service.save()

            return {"message": "Service deactivated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
