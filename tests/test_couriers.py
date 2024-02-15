from sqlalchemy import select

from conftest import client, async_session_maker
from models.couriers.courier import Courier
from scripts.generate_data import generate_couriers


def test_add_data():
    generate_couriers()


def test_add_courier():
    response = client.post("/api/courier", json={
        "sid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "Ivan",
        "districts": [
            "Moscow"
        ]
    })

    assert response.status_code == 200


def test_get_courier_list():
    response = client.get("/api/courier")

    assert response.status_code == 200


async def test_get_courier():
    async with async_session_maker() as session:
        query = select(Courier)
        result = await session.execute(query)
        result = result.scalars().all()

    courier = result[-1]

    response = client.get(f"/api/courier/{courier.sid}")

    assert response.status_code == 200

    response = client.get("/api/courier/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    assert response.status_code == 404

