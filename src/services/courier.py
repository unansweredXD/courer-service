from uuid import UUID

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

    async def get_courier_list(self):
        courier_list = await courier_repository.get_all(self.db_session)

        return courier_list

    async def get_courier(self, courier_id: UUID):
        courier_list = await courier_repository.get(self.db_session, courier_id)

        return courier_list
