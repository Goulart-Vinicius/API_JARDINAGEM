from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router.RequestRouter import router_request
from router.ServicesRouter import router_services
from router.UserRouter import router_user

app = FastAPI()

app.include_router(router_user)
app.include_router(router_services)
app.include_router(router_request)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite qualquer método (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Permite qualquer cabeçalho
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
