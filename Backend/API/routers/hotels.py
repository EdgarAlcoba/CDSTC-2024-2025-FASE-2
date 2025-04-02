from calendar import day_abbr

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from datetime import date, timedelta

from ..dao.cities import Cities
from ..dao.hotels import Hotels
from ..routers.auth import authenticate
from ..dao.hotels_occupation import HotelsOccupation
from ..dao.hotels_consumption import HotelsConsumption

router = APIRouter()

class HotelInfoRequest(BaseModel):
    date: date
    city_id: int | None = None

@router.get("/hotels")
async def get_hotels(request: Request):
    return Hotels.get_all()

@router.get("/getOccupation")
async def get_occupation(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    occupations_avg_percent = HotelsOccupation.get_occupations_avg_percent(data.date, data.city_id)
    if occupations_avg_percent is None:
        raise HTTPException(
            status_code=400, detail="City ID provided does not correspond to any city"
        )
    return {
        "occupations_avg_percent": round(occupations_avg_percent, 2)
    }

@router.get("/getReservations")
async def get_reservations(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    reservations_sum: int = HotelsOccupation.get_total_reservations(data.date, data.city_id)
    if reservations_sum is None:
        raise HTTPException(
            status_code=400, detail="City ID provided does not correspond to any city"
        )
    return {
        "reservations_sum": reservations_sum
    }

@router.get("/getCancellations")
async def get_cancellations(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    cancellations_sum: int = HotelsOccupation.get_total_cancellations(data.date, data.city_id)
    if cancellations_sum is None:
        raise HTTPException(
            status_code=400, detail="City ID provided does not correspond to any city"
        )
    return {
        "cancellations_sum": cancellations_sum
    }

@router.get("/getAveragePrice")
async def get_average_price(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    average_price: float = HotelsOccupation.get_average_price(data.date, data.city_id)
    if average_price is None:
        raise HTTPException(
            status_code=400, detail="City ID provided does not correspond to any city"
        )
    return {
        "average_price": round(average_price, 2)
    }

@router.get("/getEcoIndex")
async def get_eco_index(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    average_eco_index: float = HotelsConsumption.get_average_eco_index(data.date, data.city_id)
    top_eco_indexes: list[dict[str,any]] = HotelsConsumption.get_top_eco_indexes(data.date, data.city_id)
    if (average_eco_index is None) or (top_eco_indexes is None):
        raise HTTPException(
            status_code=400, detail="City ID provided does not correspond to any city"
        )
    return {
        "average_eco_index": round(average_eco_index, 2),
        "top_eco_hotels": top_eco_indexes
    }

@router.get("/getOccupationLast7Days")
async def get_occupation_last_7_days(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    occupation_last_7_days: list[float] = HotelsOccupation.get_occupation_days(data.date, data.city_id)
    occupation_last_7_days_array = []
    if len(occupation_last_7_days) == 0:
        raise HTTPException(status_code=500, detail="Could not find occupation for the last 7 days")
    i: int = 0
    for occupation_percent_day in occupation_last_7_days:
        occupation_last_7_days_array.append({
            "day": data.date - timedelta(days=i),
            "occupation_rate": occupation_percent_day
        })
        i += 1
    return occupation_last_7_days_array

@router.get("/getAveragePriceLast7Days")
async def get_average_price_last_7_days(data: HotelInfoRequest, request: Request):
    #authenticate(request, "admin")
    average_price_7_days: list[float] = HotelsOccupation.get_average_prices(data.date, data.city_id)
    average_price_7_days_array = []
    if len(average_price_7_days) == 0:
        raise HTTPException(status_code=500, detail="Could not find average prices for the last 7 days")
    i: int = 0
    for occupation_percent_day in average_price_7_days:
        average_price_7_days_array.append({
            "day": data.date - timedelta(days=i),
            "average_night_price": occupation_percent_day
        })
        i += 1
    return average_price_7_days_array
