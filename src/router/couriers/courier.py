from fastapi import APIRouter

from models.couriers.schemas.courier import AddCourier
from router.deps import PGSession
from services.courier import CourierService

router = APIRouter()


@router.post("/")
async def add_courier(db: PGSession, courier: AddCourier):
    result = await CourierService(db).add_courier(courier)

    return result
