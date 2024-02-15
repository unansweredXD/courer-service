import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from common.enums.enums import OrderStatus


class OrderInfoForCourier(BaseModel):
    order_id: UUID
    order_name: str


class AddOrder(BaseModel):
    name: str
    district: str


class OrderInfo(BaseModel):
    courier_id: UUID
    status: OrderStatus


class AddedOrder(BaseModel):
    order_id: UUID
    courier_id: UUID
