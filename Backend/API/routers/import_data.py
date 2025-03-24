from fastapi import APIRouter, UploadFile, Response

from ..dao.reviews import Reviews
from ..dao.services import Services
from ..utils.validate_csv import validate_all_csv_exist
from ..dao.cities import Cities
from ..dao.hotels import Hotels
from ..dao.hotels_consumption import HotelsConsumption

router = APIRouter()

@router.post("/import")
async def import_data(files: list[UploadFile], response: Response):
    files = validate_all_csv_exist(files)
    Cities.import_from_csv(files)
    Hotels.import_from_csv(files)
    HotelsConsumption.generate_sustainability_indexes()
    Services.import_from_csv(files)
    Reviews.import_from_csv(files)
    return "OK"



