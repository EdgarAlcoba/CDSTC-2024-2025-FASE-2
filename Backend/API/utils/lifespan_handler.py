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
    ai_ok_filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Storage', 'ai_ok'))
    if not os.path.isfile(ai_ok_filepath):
        print("Generating AI database")
        init_db_ai()
        with open(ai_ok_filepath, "w") as f:
            pass

def on_server_stop(app: FastAPI):
    x = 0

@asynccontextmanager
async def lifespan(app: FastAPI):
    on_server_start(app)
    yield
    on_server_stop(app)