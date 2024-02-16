from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.repository import AbstractRepository
from models.orders.order import Order


class OrderRepository(AbstractRepository[Order]):
    async def get_all_by_courier_id(self, session: AsyncSession, courier_id: UUID):
        objs = await session.execute(
            select(self._t_model)
            .order_by(self._t_model.completed.desc())
            .filter(self._t_model.courier_sid == courier_id)
        )
        return list(objs.scalars().all())


order_repository = OrderRepository(Order)
