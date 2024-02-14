import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderInfoForCourier(BaseModel):
    order_id: UUID
    order_name: str
