from fastapi import APIRouter, Request
from pydantic import BaseModel
from datetime import date

from Backend.API.routers.auth import authenticate
from ..dao.hotels_occupation import HotelsOccupation
from ..dao.hotels_consumption import HotelsConsumption

router = APIRouter()

class GetOccupationData(BaseModel):
    date: date
    city_id: int | None = None

@router.get("/getOccupation")
async def get_occupation(data: GetOccupationData, request: Request):
    authenticate(request, "admin")
    return round(HotelsOccupation.get_occupations_avg_percent(data.date), 2)

@router.get("/getCancellations")
async def get_occupation(data: GetOccupationData, request: Request):
    authenticate(request, "admin")
    return HotelsOccupation.get_total_cancellations(data.date)

@router.get("/getAveragePrice")
async def get_occupation(data: GetOccupationData, request: Request):
    authenticate(request, "admin")
    return round(HotelsOccupation.get_average_price(data.date), 2)

@router.get("/getEcoIndex")
async def get_occupation(data: GetOccupationData, request: Request):
    authenticate(request, "admin")
    return round(HotelsConsumption.get_average_eco_index(data.date), 2)