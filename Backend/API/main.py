from fastapi import FastAPI

from .routers import import_data
from .utils import lifespan_handler

app = FastAPI(lifespan=lifespan_handler.lifespan)

app.include_router(import_data.router)