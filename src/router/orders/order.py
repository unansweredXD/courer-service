from uuid import UUID

from fastapi import APIRouter, HTTPException

from common.enums.enums import OrderStatus
from models.orders.schemas.order import AddOrder, OrderInfo, AddedOrder
from router.deps import PGSession
from services.courier import CourierService
from services.order import OrderService

router = APIRouter()


@router.post('/', response_model=AddedOrder)
async def add_order(
        db: PGSession,
        order: AddOrder
):
    """ Добавление нового заказа, при наличии свободных курьеров """

    order_data = await OrderService(db).add_order(order)

    return order_data


@router.get('/{order_id}', response_model=OrderInfo)
async def get_order(
        db: PGSession,
        order_id: UUID
):
    """ Получение информации о заказе """

    order = await OrderService(db).get_order(order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail='Заказ с таким id не найден!'
        )

    return OrderInfo(courier_id=order.courier_sid, status=order.status)


@router.post('/{order_id}')
async def complete_order(
        db: PGSession,
        order_id: UUID
):
    """ Завершение заказа и выполнение необходимых вычислений для статистики курьера """

    order_service = OrderService(db)

    order = await order_service.get_order(order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail='Заказ с таким id не найден!'
        )

    if order.status == OrderStatus.complete:
        raise HTTPException(
            status_code=404,
            detail='Этот заказ уже завершен!'
        )

    completed_order = await order_service.complete_order(order)

    await CourierService(db).complete_order_courier(completed_order)

    return {
        'status': 'success'
    }
