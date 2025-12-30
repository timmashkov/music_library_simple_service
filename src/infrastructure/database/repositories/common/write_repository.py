from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

from bson import ObjectId

from infrastructure.database.database_adapter import MongoDatabaseAdapter

T = TypeVar("T")
M = TypeVar("M")


class _CommonMongoWriteRepository(Generic[T, M], ABC):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter, collection_name: str):
        self.mongo_adapter = mongo_adapter
        self.collection_name = collection_name

    @abstractmethod
    def _to_model(self, entity: T) -> M:
        pass

    async def create_item(self, entity: T) -> T:
        model = self._to_model(entity)

        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            await collection.insert_one(model.dict(by_alias=True), session=session)

            return entity

    async def update_item(self, entity: T) -> T:
        model = self._to_model(entity)

        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            await collection.update_one(
                {"_id": model.id},
                {"$set": model.dict(by_alias=True, exclude={"id"})},
                session=session,
            )
            return entity

    async def delete_item(self, item_id: str) -> bool:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            result = await collection.delete_one(
                {"_id": ObjectId(item_id)}, session=session
            )
            return result.deleted_count > 0
