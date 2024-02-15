import datetime
from uuid import UUID

from fastapi import HTTPException

from common.enums.enums import OrderStatus
from models.couriers.repository.courier import courier_repository
from models.orders.order import Order
from models.orders.repository.order import order_repository
from models.orders.schemas.order import AddOrder, AddedOrder, OrderInfo
from services.abstract import AbstractService


class OrderService(AbstractService):
    async def add_order(self, order: AddOrder):
        free_courier = await courier_repository.get_free(self.db_session, order.district)

        if not free_courier:
            raise HTTPException(
                status_code=404,
                detail='Свободный курьер в этом районе не найден!',
            )

        new_order = Order()
        new_order.name = order.name
        new_order.district = order.district
        new_order.courier_sid = free_courier.sid

        order = await order_repository.create(self.db_session, new_order)

        changes = {
            'order_sid': order.sid
        }

        await courier_repository.update(self.db_session, free_courier, changes)

        return AddedOrder(order_id=order.sid, courier_id=free_courier.sid)

    async def get_order(self, order_id: UUID):
        order = await order_repository.get(self.db_session, order_id)

        return order

    async def complete_order(self, order: Order):
        changes = {
            'status': OrderStatus.complete,
            'completed': datetime.datetime.utcnow()
        }

        completed_order = await order_repository.update(self.db_session, order, changes)

        return completed_order
