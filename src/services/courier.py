from sqlalchemy.ext.asyncio import AsyncSession

from models.couriers.courier import Courier
from models.couriers.repository.courier import courier_repository


class CourierService:
    def __init__(self, db_session: AsyncSession):
        self.db_session: AsyncSession = db_session

    async def add_courier(self, input_courier):
        courier = Courier()

        courier.name = input_courier.name
        courier.districts = input_courier.districts

        result = await courier_repository.create(self.db_session, courier)

        return result
