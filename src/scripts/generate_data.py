import datetime
import random

from faker import Faker
import psycopg2
import psycopg2.extras

import uuid
from random import choice

import settings


faker = Faker()
psycopg2.extras.register_uuid()

districts_list = [
    ['Moscow', 'Saint-Petersburg'], ['Barnaul', 'Tomsk'], ['Barnaul', 'Moscow'], ['Tomsk', 'Saint-Petersburg'],
    ['Tomsk', 'Moscow'], ['Moscow', 'Saint-Petersburg'], ['Barnaul', 'Tomsk'], ['Barnaul', 'Moscow'],
    ['Tomsk', 'Saint-Petersburg'], ['Tomsk', 'Moscow']
]

couriers_dct = {}


def generate_couriers():
    conn = psycopg2.connect(
        f"host={settings.HOST_WIN} port={settings.POSTGRES_PORT} "
        f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}")
    conn.autocommit = True
    cur = conn.cursor()

    for _ in range(10):
        sid = uuid.uuid4()
        districts = choice(districts_list)
        couriers_dct[sid] = districts
        query = (f"INSERT INTO couriers (sid, name, districts, avg_day_orders, avg_order_complete_time) "
                 f"VALUES ('{sid}', '{faker.name()}', ARRAY{districts}, '0', '{datetime.time(0, 0, 0)}');")

        cur.execute(query)
    conn.commit()


def generate_orders():
    conn = psycopg2.connect(
        f"host={settings.HOST_WIN} port={settings.POSTGRES_PORT} "
        f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}")
    conn.autocommit = True
    cur = conn.cursor()

    try:
        for courier_sid, districts in couriers_dct.items():
            order_sid = uuid.uuid4()
            cur.execute(
                f"INSERT INTO orders (sid, name, district, status, courier_sid, created) "
                f"VALUES ('{order_sid}', '{faker.word()}', '{choice(districts)}', 'in_progress', '{courier_sid}', "
                f"'{datetime.datetime.utcnow() - datetime.timedelta(hours=random.randint(1, 10))}');"
            )

            cur.execute(
                f"UPDATE couriers SET active_order = '{order_sid}' WHERE sid = '{courier_sid}';"
            )

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

    conn.commit()


if __name__ == "__main__":
    generate_couriers()
    generate_orders()
