from fastapi import HTTPException
from model.schemas import ServicesSchema

from model.ServicesModel import Services


class ServicesController:

    def __init__(self):
        self.Services = Services()

    def get_all(self):
        try:
            return self.Services.select().get()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")