import datetime
from uuid import UUID

from pydantic import BaseModel


class CourierBase(BaseModel):
    name: str


class AddCourier(CourierBase):
    districts: list[str]
