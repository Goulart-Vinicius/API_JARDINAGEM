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
        except:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get(self, request_id: int):
        try:
            request = self.Request.get_by_id(request_id)

            return RequestSchema.model_validate(request).model_dump()

        except Exception as e:
            if "instance matching query does not exist" in str(e):
                raise HTTPException(status_code=404, detail='Service not found')
            HTTPException(status_code=500, detail="Internal Server Error")

    def add(self, request: RequestSchema):
        try:
            request_data = request.model_dump()
            request_model = self.Request.create(**request_data)
            request_validated = RequestSchema.model_validate(request_model)
            service = request_validated.service
            gardner = request_validated.gardner
            client = request_validated.client

            request_validated.service = service.id
            request_validated.gardner = gardner.id
            request_validated.client = client.id

            return request_validated.model_dump()
        except Exception as e:
            if 'UNIQUE constraint failed: services.name' in str(e):
                raise HTTPException(status_code=409, detail="Service already exists")
            HTTPException(status_code=500, detail='Internal Server Error')

    def update(self, request_id: int, request_data: RequestSchema):
        try:
            request_data = request_data.model_dump()
            request = self.Request.get_by_id(request_id)

            request.client = request_data['client']
            request.date = request_data['date']
            request.service = request_data['service']
            request.gardner = request_data['gardner']

            request.save()
            return RequestSchema.model_validate(self.get(request_id)).model_dump()
        except Exception as e:

            if str(e) == 'UNIQUE constraint failed: services.name':
                raise HTTPException(status_code=409, detail="Service name already exists")
            else:
                raise HTTPException(status_code=500, detail=str(e))

    def delete(self, request_id: int):
        try:
            request = self.Request.get_by_id(request_id)

            request.active = False
            request.save()

            return {"message": "Request canceled successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
