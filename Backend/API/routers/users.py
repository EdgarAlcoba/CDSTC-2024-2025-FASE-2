from fastapi import APIRouter, Request
import base64

from Backend.API.routers.auth import authenticate
from ..dto.user import User

router = APIRouter()

@router.get("/user/info")
async def get_occupation(request: Request):
    user: User = authenticate(request, "basic")
    return {
        "name": user.name,
        "surname": user.surname,
        "email": user.email,
        "profile_picture": base64.b64encode(user.profile_picture.encode("utf-8")),
        "mock": user.mock,
        "role": user.role
    }