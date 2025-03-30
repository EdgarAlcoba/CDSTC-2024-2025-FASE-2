from fastapi import APIRouter, UploadFile, Request

from ..dao.reviews import Reviews
from ..dao.services import Services
from ..dao.touristic_routes import TouristicRoutes
from ..dao.transport_usages import TransportUsages
from ..dao.cities import Cities
from ..dao.hotels import Hotels
from ..dao.hotels_consumption import HotelsConsumption
from ..utils.validate_csv import validate_all_csv_exist
from ..routers.auth import authenticate

router = APIRouter()

@router.post("/import", status_code=204)
async def import_data(files: list[UploadFile], request: Request):
    authenticate(request, "admin")
    files = validate_all_csv_exist(files)
    Cities.import_from_csv(files)
    Hotels.import_from_csv(files)
    HotelsConsumption.generate_sustainability_indexes()
    Services.import_from_csv(files)
    Reviews.import_from_csv(files)
    TouristicRoutes.import_from_csv(files)
    TransportUsages.import_from_csv(files)



