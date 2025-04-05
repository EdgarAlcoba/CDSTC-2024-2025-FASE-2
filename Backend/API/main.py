from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth
from .routers import import_data
from .routers import hotels
from .routers import users
from .routers import cities
from .routers import services

from .utils import lifespan_handler

app = FastAPI(lifespan=lifespan_handler.lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["authorization", "content-type"],
)

app.include_router(import_data.router)
app.include_router(auth.router)
app.include_router(hotels.router)
app.include_router(cities.router)
app.include_router(services.router)
app.include_router(users.router)