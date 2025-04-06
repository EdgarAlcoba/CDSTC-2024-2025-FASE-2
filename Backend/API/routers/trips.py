from fastapi import APIRouter, Request, Response, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json

from ..routers.auth import authenticate
from ..dto.user import User
from ..dao.cities import Cities
from ..dao.users import Users
from ..dao.trips import Trips
from ..utils.jwt import JWT
from ..ai.generate_itinerary import generate_itinerary
router = APIRouter()

class PlanTripData(BaseModel):
    destination: str
    transport: str
    activities: list[str]
    budget: str
    duration: int
    considerations: str

def validate_plan_trip_data(data: PlanTripData):
    if not data.destination:
        raise HTTPException(status_code=400, detail="destination cannot be empty")
    if not data.transport:
        raise HTTPException(status_code=400, detail="transport cannot be empty")
    if not len(data.activities):
        raise HTTPException(status_code=400, detail="activities cannot be empty")
    for activity in data.activities:
        if not activity:
            raise HTTPException(status_code=400, detail="all activities inside activities cannot be empty")
    if not data.budget:
        raise HTTPException(status_code=400, detail="budget cannot be empty")
    if not data.duration:
        raise HTTPException(status_code=400, detail="duration cannot be empty")
    if not data.considerations:
        raise HTTPException(status_code=400, detail="considerations cannot be empty")

def plan_trip_ai(destination: str, transport: str, activities: list[str], budget: str, duration: int, considerations: str):
    destination_city = Cities.find_by_name(destination)
    if not destination_city:
        raise HTTPException(status_code=400, detail=f"Destination city {destination} not found")
    activities_str = ""
    for i in range(0, len(activities)):
        if i == len(activities)-1:
            activities_str += f"{activities[i]}"
        else:
            activities_str += f"{activities[i]}, "

    ai_response_raw = generate_itinerary(
        destination=destination,
        destination_description=destination_city.description,
        duration=duration,
        transport_preference=transport,
        type_of_tourism=activities_str,
        budget=budget,
        user_interests=considerations
    )

    ai_response_clean = ai_response_raw.removeprefix('```json').removesuffix('```')

    return json.loads(ai_response_clean)

@router.post("/planTrip")
async def plan_trip(data: PlanTripData, request: Request, response: Response):
    user: User = authenticate(request)
    validate_plan_trip_data(data)
    ai_response: object = plan_trip_ai(
        data.destination, data.transport,
        data.activities, data.budget, data.duration,
        data.considerations
    )
    trip_data = Trips.add(user, ai_response)
    ai_response["id"] = trip_data[0]
    ai_response["generated_on"] = trip_data[1]
    return ai_response
@router.get("/trips")
async def get_trips(request: Request):
    user: User = authenticate(request)
    return Trips.get_all(user)



