import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from models.orders.schemas.order import OrderInfoForCourier


class CourierBase(BaseModel):
    sid: Optional[UUID]
    name: str


class AddCourier(CourierBase):
    districts: list[str]


class CourierInfo(CourierBase):
    districts: list[str]
    avg_day_orders: int
    avg_order_complete_time: datetime.time
    active_order: Optional[OrderInfoForCourier | None]
