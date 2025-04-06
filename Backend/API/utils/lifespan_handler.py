import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
import os.path

from ..dao.reviews import Reviews
from ..utils.db import init_db
from ..utils.constants import init as init_constants
from ..dao.cities import Cities
from ..dao.reviews import Reviews
from ..ai.generate_embeddings import init_db_ai
from ..ai.generate_itinerary import generate_itinerary

def on_server_start(app: FastAPI):
    init_constants()
    init_db()
    try:
        init_db_ai()
    except Exception as e:
        if e.status_code != 409:
            raise RuntimeError(f"AI error: {e}")

def on_server_stop(app: FastAPI):
    x = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    on_server_start(app)
    yield
    on_server_stop(app)