import datetime
import uuid

from sqlalchemy import String, ForeignKey, Integer, UUID, ARRAY, Time
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel
from models.orders.order import Order


class Courier(BaseModel):
    __tablename__ = 'couriers'

    sid = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=lambda: uuid.uuid4().hex
    )

    name = mapped_column(String, nullable=False)

    districts = mapped_column(ARRAY(String), nullable=False)

    active_order = mapped_column(ForeignKey('orders.sid', use_alter=True), nullable=True)

    avg_day_orders = mapped_column(Integer, nullable=False, default=0)

    avg_order_complete_time = mapped_column(Time, nullable=False, default=datetime.time(0, 0, 0))

    order = relationship(
        Order, foreign_keys=[active_order], lazy="joined"
    )
