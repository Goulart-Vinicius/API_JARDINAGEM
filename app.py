from fastapi import FastAPI
from router.UserRouter import router_user

app = FastAPI()  # Instanciação correta do FastAPI

app.include_router(router_user)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
