from fastapi import FastAPI
from contextlib import asynccontextmanager

from ..dao.reviews import Reviews
from ..utils.db import init_db
from ..utils.constants import init as init_constants
from ..dao.cities import Cities
from ..dao.reviews import Reviews

def on_server_start(app: FastAPI):
    init_constants()
    init_db()

def on_server_stop(app: FastAPI):
    x = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    on_server_start(app)
    yield
    on_server_stop(app)