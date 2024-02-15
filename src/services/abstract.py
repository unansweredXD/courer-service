from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractService(ABC):
    def __init__(self, db_session: AsyncSession):
        self.db_session: AsyncSession = db_session
