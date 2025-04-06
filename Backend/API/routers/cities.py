from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from datetime import date

from ..dao.cities import Cities
from ..routers.auth import authenticate

router = APIRouter()

class HotelInfoRequest(BaseModel):
    city_name: str
    date: date

@router.get("/cities")
async def get_cities():
    #authenticate(request, "admin")
    return Cities.get_all()

@router.get("/cities/hotelRatings")
async def get_cities_hotel_ratings():
    return Cities.get_hotel_ratings()

@router.post("/cities/info")
async def get_cities_info(data: HotelInfoRequest):
    return Cities.get_info(data.city_name, data.date)