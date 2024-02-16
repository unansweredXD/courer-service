from uuid import UUID

from fastapi import APIRouter, HTTPException

from models.couriers.schemas.courier import AddCourier, CourierBase, CourierInfo
from models.orders.schemas.order import OrderInfoForCourier
from router.deps import PGSession
from services.courier import CourierService

router = APIRouter()


@router.post("/")
async def add_courier(
        db: PGSession,
        courier: AddCourier
):
    """ Добавление нового курьера в систему. Необходима информация об имени курьера, а также о райнах, в которых он
    работает """

    result = await CourierService(db).add_courier(courier)

    return result


@router.get("/", response_model=list[CourierBase])
async def get_courier_list(
        db: PGSession
):
    """ Получение информации о всех курьерах, зарегистрированных в системе """

    courier_list = await CourierService(db).get_courier_list()

    return courier_list


@router.get("/{courier_id}", response_model=CourierInfo)
async def get_courier_info(
        db: PGSession,
        courier_id: UUID
):
    """ Получение полной информации о курьере и его активном заказе по идентификатору курьера """

    courier_info = await CourierService(db).get_courier(courier_id)

    if not courier_info:
        raise HTTPException(
            status_code=404,
            detail='Курьер с таким id не найден!',
        )

    if courier_info.active_order is not None:
        active_order = OrderInfoForCourier(order_id=courier_info.order.sid, order_name=courier_info.order.name)

        courier_info.active_order = active_order

    return courier_info
