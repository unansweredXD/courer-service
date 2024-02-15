from sqlalchemy import select

from conftest import client, async_session_maker
from models.couriers.courier import Order
from scripts.generate_data import generate_orders


def test_add_data():
    generate_orders()


def test_add_courier():
    response = client.post("/api/order", json={
        "name": "test_name",
        "district": "Moscow"
    })

    assert response.status_code == 200

    response = client.post("/api/order", json={
        "name": "test_name",
        "district": "Alabama"
    })

    assert response.status_code == 404


async def test_get_order():
    async with async_session_maker() as session:
        query = select(Order)
        result = await session.execute(query)
        result = result.scalars().all()

    order = result[-1]

    response = client.get(f"/api/order/{order.sid}")

    assert response.status_code == 200

    response = client.get("/api/order/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    assert response.status_code == 404


async def test_complete_order():
    async with async_session_maker() as session:
        query = select(Order)
        result = await session.execute(query)
        result = result.scalars().all()

    order = result[-1]

    response = client.post(f"/api/order/{order.sid}")

    assert response.status_code == 200

    response = client.post("/api/order/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    assert response.status_code == 404
