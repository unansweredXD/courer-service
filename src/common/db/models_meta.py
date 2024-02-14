from common.db.base_model import BaseModel

# include models here

from models.couriers.courier import Courier
from models.orders.order import Order


metadata = BaseModel.metadata
