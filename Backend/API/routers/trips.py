from fastapi import APIRouter, Request, Response, HTTPException
from pydantic import BaseModel
from datetime import datetime

from ..routers.auth import authenticate
from ..dto.user import User
from ..dao.users import Users
from ..dao.trips import Trips
from ..utils.jwt import JWT
router = APIRouter()

class PlanTripData(BaseModel):
    destination: str
    transport: str
    activities: list[str]
    budget: str
    duration: int

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

def validate_trip_ai_response(ai_response: object):
    if ('destination' not in ai_response) or (ai_response['destination'] == ''):
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a destination string field")
    if ('duration' not in ai_response) or (ai_response["duration"] == ''):
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a duration integer field")
    duration: int = 0
    try:
        duration: int = int(ai_response['duration'])
    except ValueError:
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a valid duration. Must be an integer field")
    if ('budget' not in ai_response) or (ai_response["budget"] == ""):
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a budget string field")
    if ai_response['budget'] not in ['High', 'Medium', 'Low']:
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a valid budget string. Must be either High, Medium or Low")
    if ('itinerary' not in ai_response) or (ai_response["itinerary"] == ""):
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a itinerary list field")
    if type(ai_response["itinerary"]) != list:
        raise HTTPException(status_code=500, detail="Trip AI response does not contain a valid itinerary list")
    itinerary: list = ai_response["itinerary"]
    if len(itinerary) != duration:
        raise HTTPException(status_code=500, detail=f"Trip AI response does not contain a valid itinerary list length. Got {len(itinerary)} planned days for requested {duration} days")
    for i in range(0, len(itinerary)):
        day = itinerary[i]
        if ('day' not in day) or (day['day'] == ''):
            raise HTTPException(status_code=500, detail=f"Trip AI response does not contain a valid itinerary list: day key not found on itinerary {i} object")
        try:
            day_number: int = int(day['day'])
            if day_number != i+1:
                raise ValueError
            if 'activities' not in day:
                raise HTTPException(
                    status_code=500,
                    detail=f"Trip AI response day {day_number} does not contain an activities key on itinerary {i} object"
                )
            if type(day["activities"]) != list:
                raise HTTPException(
                    status_code=500,
                    detail=f"Trip AI response day {day_number} does not contain a valid activities list on itinerary {i} object"
                )
            activities: list = day["activities"]
            for j in range(0, len(activities)):
                activity = activities[j]
                if ('time' not in activity) or (activity['time'] == ''):
                    raise HTTPException(
                        status_code=500,
                        detail=f"Trip AI response activity {j} on day {day_number} does not contain an time string on itinerary {i} object"
                    )
                try:
                    datetime.strptime(activity["time"], "%I:%M %p")
                except ValueError:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Trip AI response activity {j} on day {day_number} does not contain a valid time string on itinerary {i} object"
                    )
                if ('activity' not in activity) or (activity['activity'] == ''):
                    raise HTTPException(
                        status_code=500,
                        detail=f"Trip AI response activity {j} on day {day_number} does not contain an activity string on itinerary {i} object"
                    )
                if ('details' not in activity) or (activity['details'] == ''):
                    raise HTTPException(
                        status_code=500,
                        detail=f"Trip AI response activity {j} on day {day_number} does not contain an details string on itinerary {i} object"
                    )
                if ('location' not in activity) or (activity['location'] == ''):
                    raise HTTPException(
                        status_code=500,
                        detail=f"Trip AI response activity {j} on day {day_number} does not contain an location string on itinerary {i} object"
                    )

        except ValueError:
            raise HTTPException(status_code=500, detail=f"Trip AI response does not contain a valid itinerary list: day key is not a correct integer on itinerary {i} object")

def plan_trip_ai(destination: str, transport: str, activities: list[str], budget: str, duration: int):
    return {
        "destination": "Aruba Central",
        "duration": 2,
        "budget": "High",
        "itinerary": [
            {
                "day": 1,
                "activities": [
                    {
                        "time": "09:00 AM",
                        "activity": "Check-in at Aruba Luxury Lodge",
                        "details": "Enjoy a complimentary welcome drink and a brief tour of the amenities.",
                        "location": "Aruba Luxury Lodge"
                    },
                    {
                        "time": "11:00 AM",
                        "activity": "Bicycle Tour of Arikok National Park",
                        "details": "Guided cycling adventure through rugged terrains and stunning landscapes.",
                        "location": "Arikok National Park"
                    },
                    {
                        "time": "02:00 PM",
                        "activity": "Lunch at Elements Restaurant",
                        "details": "Enjoy a gourmet meal with a focus on organic and local ingredients.",
                        "location": "Elements Restaurant"
                    },
                    {
                        "time": "04:00 PM",
                        "activity": "Snorkeling Adventure",
                        "details": "Discover the vibrant marine life in crystal clear waters.",
                        "location": "Mangel Halto"
                    },
                    {
                        "time": "07:00 PM",
                        "activity": "Dinner at Passions on the Beach",
                        "details": "Dine under the stars with a beautiful sunset view.",
                        "location": "Passions on the Beach"
                    }
                ]
            },
            {
                "day": 2,
                "activities": [
                    {
                        "time": "09:30 AM",
                        "activity": "Bicycle to the Butterfly Farm",
                        "details": "Experience the tranquility of wandering through a tropical garden with butterflies.",
                        "location": "The Butterfly Farm"
                    },
                    {
                        "time": "12:00 PM",
                        "activity": "Lunch at Yemanja Woodfired Grill",
                        "details": "Taste the exotic flavors and wood-fired dishes.",
                        "location": "Yemanja Woodfired Grill"
                    },
                    {
                        "time": "02:30 PM",
                        "activity": "Bicycle to Alto Vista Chapel",
                        "details": "Visit the historical and spiritual chapel and enjoy the serene surroundings.",
                        "location": "Alto Vista Chapel"
                    },
                    {
                        "time": "06:00 PM",
                        "activity": "Sunset Sailing Excursion",
                        "details": "Luxury catamaran tour with cocktails and snacks.",
                        "location": "Palm Beach Marina"
                    },
                    {
                        "time": "08:30 PM",
                        "activity": "Dinner at Barefoot Restaurant",
                        "details": "Fine dining with your toes in the sand.",
                        "location": "Barefoot Restaurant"
                    }
                ]
            }
        ]
    }

@router.post("/planTrip")
async def plan_trip(data: PlanTripData, request: Request, response: Response):
    user: User = authenticate(request)
    validate_plan_trip_data(data)
    ai_response: object = plan_trip_ai(
        data.destination, data.transport,
        data.activities, data.budget, data.duration
    )
    validate_trip_ai_response(ai_response)
    trip_data = Trips.add(user, ai_response)
    ai_response["id"] = trip_data["id"]
    ai_response["generated_on"] = trip_data["created_at"]
    return ai_response
@router.get("/trips")
async def get_trips(request: Request):
    user: User = authenticate(request)
    return Trips.get_all(user)



