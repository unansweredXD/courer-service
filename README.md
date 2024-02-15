# courer-service

REST API сервис для распределения заказов между курьерами

**Для того, чтобы запустить и протестировать окружение, необходимо прописать в консоли следующее:**

```
    pip install -r requirements.txt
    docker-compose up --build
    pytest tests/
```

**Для того, чтобы запустить и настроить окружение для ручных тестов, необходимо прописать в консоли следующее:**

```
    docker-compose up -d
    alembic upgrade head
```

Затем необходимо запустить файл src/scripts/generate_data.py для генерации данных

Также можно переходить по адресу http://localhost:8000/docs для доступа к сваггеру

*Примечание: если ручные тесты запускаются после pytest, то миграции не нужны*