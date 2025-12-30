from contextlib import asynccontextmanager
from typing import AsyncGenerator

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorClientSession,
    AsyncIOMotorCollection,
)


class MongoDatabaseAdapter:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database_name: str,
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.database_name = database_name
        self.password = password
        self._client: AsyncIOMotorClient = AsyncIOMotorClient(
            self.db_url, authSource="admin"
        )
        self._database = self._client[database_name]

    @property
    def db_url(self) -> str:
        return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}authSource=admin"

    @asynccontextmanager
    async def open_session(self) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        session = await self._client.start_session()
        try:
            yield session
        finally:
            await session.end_session()

    async def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        return self._database[collection_name]
