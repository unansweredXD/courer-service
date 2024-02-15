import datetime
from uuid import UUID

from models.couriers.courier import Courier
from models.couriers.repository.courier import courier_repository
from models.couriers.schemas.courier import AddCourier
from models.orders.order import Order
from models.orders.repository.order import order_repository
from services.abstract import AbstractService


class CourierService(AbstractService):
    async def add_courier(self, input_courier: AddCourier):
        courier = Courier()

        courier.name = input_courier.name
        courier.districts = input_courier.districts

        result = await courier_repository.create(self.db_session, courier)

        return result

    async def get_courier_list(self):
        courier_list = await courier_repository.get_all(self.db_session)

        return courier_list

    async def get_courier(self, courier_id: UUID):
        courier_list = await courier_repository.get(self.db_session, courier_id)

        return courier_list

    async def complete_order_courier(self, order: Order):
        courier = await courier_repository.get(self.db_session, order.courier_sid)

        order_list = await order_repository.get_all_by_courier_id(self.db_session, courier.sid)

        new_avg_time = self.get_new_avg_time(
            order.completed,
            order.created,
            courier.avg_order_complete_time,
            len(order_list)
        )

        new_avg_time = (datetime.datetime.min + new_avg_time).time()

        new_avg_orders = self.get_new_avg_orders(len(order_list), order_list)

        print(new_avg_orders)

        changes = {
            'order_sid': None,
            'avg_orders': new_avg_orders,
            'avg_order_time': new_avg_time
        }

        await courier_repository.update(self.db_session, courier, changes)

    @staticmethod
    def get_new_avg_time(
            order_completed: datetime,
            order_created: datetime,
            avg_order_time: datetime,
            count_orders: int
    ) -> datetime.timedelta:
        """ Метод пересчитывает среднее время выполнения заказа, с учетом текущего """

        order_duration = (order_completed - order_created).total_seconds()

        total_seconds = (avg_order_time.hour * 60 + avg_order_time.minute) * 60 + avg_order_time.second

        new_avg_time = int((total_seconds * (count_orders - 1) + order_duration) / count_orders)

        return datetime.timedelta(seconds=new_avg_time)

    @staticmethod
    def get_new_avg_orders(order_count: int, order_list: list[Order]) -> int:
        count_days = 1
        current_day = None

        for order in order_list:
            if current_day is None:
                # метод вызван -> как минимум один заказ завершен
                current_day = order.completed.date()
                continue

            if current_day != order.completed.date():  # сменился день
                count_days += 1
                current_day = order.completed.date()  # новая дата

        return int(order_count / count_days)
