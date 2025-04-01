from fastapi import FastAPI

from .routers import auth
from .routers import import_data
from .routers import hotels
from .routers import users
from .routers import cities
from .routers import services

from .utils import lifespan_handler

app = FastAPI(lifespan=lifespan_handler.lifespan)

app.include_router(import_data.router)
app.include_router(auth.router)
app.include_router(hotels.router)
app.include_router(cities.router)
app.include_router(services.router)
app.include_router(users.router)