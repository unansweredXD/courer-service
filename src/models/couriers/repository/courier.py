from common.repository.repository import AbstractRepository
from models.couriers.courier import Courier


class CourierRepository(AbstractRepository[Courier]):
    pass


courier_repository = CourierRepository(Courier)
