from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

from bson import ObjectId

from infrastructure.database.database_adapter import MongoDatabaseAdapter

T = TypeVar("T")


class _CommonMongoReadRepository(Generic[T], ABC):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter, collection_name: str):
        self.mongo_adapter = mongo_adapter
        self.collection_name = collection_name

    async def get_item(self, item_id: str) -> Optional[T]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            return await collection.find_one(
                {"_id": ObjectId(item_id)}, session=session
            )

    async def find(self, filters: Dict[str, Any] = None) -> List[T]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            cursor = collection.find(filters or {}, session=session)

            results = []
            async for doc in cursor:
                results.append(doc)
            return results

    async def find_one_by_field(self, field: str, value: Any) -> Optional[T]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            return await collection.find_one({field: value}, session=session)
