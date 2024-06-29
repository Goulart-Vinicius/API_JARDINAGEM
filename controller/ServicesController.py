from fastapi import HTTPException

from model.ServicesModel import Services
from model.schemas import ServicesSchema


class ServicesController:

    def __init__(self):
        self.Services = Services()

    def get_all(self):
        try:
            query = self.Services.select().where(Services.active == True)
            registros_servicos = list(query.dicts())
            servicos = [ServicesSchema.model_validate(registro).model_dump() for registro in registros_servicos]

            return servicos
        except:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get(self, id_service: int):
        try:
            service = self.Services.get_by_id(id_service)

            return ServicesSchema.model_validate(service).model_dump()

        except Exception as e:
            if "instance matching query does not exist" in str(e):
                raise HTTPException(status_code=404, detail='Service not found')
            HTTPException(status_code=500, detail="Internal Server Error")

    def add(self, service: ServicesSchema):
        try:
            service_data = service.model_dump()
            service_model = self.Services.create(**service_data)
            service_validated = ServicesSchema.model_validate(service_model)
            user = service_validated.user
            service_validated.user = user.id
            return service_validated.model_dump()
        except Exception as e:
            if 'UNIQUE constraint failed: services.name' in str(e):
                raise HTTPException(status_code=409, detail="Service already exists")
            HTTPException(status_code=500, detail='Internal Server Error')

    def update(self, service_id: int, service_data: ServicesSchema):
        try:
            service_data = service_data.model_dump()
            service = self.Services.get_by_id(service_id)

            service.name = service_data['name']
            service.price = service_data['price']
            service.time = service_data['time']
            service.user = service_data['user']

            service.save()
            return ServicesSchema.model_validate(self.get(service_id)).model_dump()
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

    def get_by_name(self, name):
        try:
            service = self.Services.select().where(self.Services.name == name).get()
            return ServicesSchema.model_validate(service).model_dump()
        except Exception as e:
            HTTPException(status_code=500, detail=str(e))
