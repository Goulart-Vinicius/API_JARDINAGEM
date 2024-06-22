from fastapi import FastAPI
from router.UserRouter import router_user
from router.ServicesRouter import router_services

app = FastAPI()  # Instanciação correta do FastAPI

app.include_router(router_user)
app.include_router(router_services)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
