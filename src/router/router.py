from fastapi import APIRouter
from router.couriers import courier
from router.orders import order

router = APIRouter()
router.include_router(courier.router, tags=["Курьеры"], prefix="/courier")
router.include_router(order.router, tags=["Заказы"], prefix="/order")
