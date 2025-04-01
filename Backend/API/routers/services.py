from fastapi import APIRouter, Request, HTTPException

from ..dao.services import Services
from ..routers.auth import authenticate

router = APIRouter()

@router.get("/services")
async def get_services(request: Request):
    authenticate(request, "admin")
    return Services.get_all()