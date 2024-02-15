from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.repository import AbstractRepository
from models.couriers.courier import Courier


class CourierRepository(AbstractRepository[Courier]):
    async def get_free(self, session: AsyncSession, district: str) -> Courier:
        obj = await session.execute(
            select(self._t_model).filter(self._t_model.active_order.is_(None), self._t_model.districts.any(district))
        )
        return obj.scalar()


courier_repository = CourierRepository(Courier)
