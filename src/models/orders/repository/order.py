from common.repository.repository import AbstractRepository
from models.orders.order import Order


class OrderRepository(AbstractRepository[Order]):
    pass


order_repository = OrderRepository(Order)
