import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
PORT: int = int(os.environ.get("PORT"))

ON_PRODUCTION: bool = False
SECRET_KEY = "secret"

POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
