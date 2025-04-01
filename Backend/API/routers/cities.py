from fastapi import APIRouter, Request, HTTPException

from Backend.API.dao.cities import Cities
from ..routers.auth import authenticate

router = APIRouter()

@router.get("/cities")
async def get_cities(request: Request):
    authenticate(request, "admin")
    return Cities.get_all()

@router.get("/cities/hotelRatings")
async def get_cities_hotel_ratings(request: Request):
    authenticate(request, "admin")
    return Cities.get_hotel_ratings()