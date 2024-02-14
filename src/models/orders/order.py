import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, UUID, Enum, DateTime
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel
from common.enums.enums import OrderStatus


class Order(BaseModel):
    __tablename__ = 'orders'

    id = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=lambda: uuid.uuid4().hex
    )

    name = mapped_column(String, nullable=False)

    status = mapped_column(Enum(OrderStatus, name='order_status', create_type=False),
                           nullable=False, default=OrderStatus.in_progress)

    district = mapped_column(String, nullable=False)

    courier_id = mapped_column(ForeignKey('couriers.id', use_alter=True))

    created = mapped_column(DateTime, default=datetime.utcnow)

    completed = mapped_column(DateTime, nullable=True)
