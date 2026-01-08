from typing import Any

from bson import ObjectId

from infrastructure.database.database_adapter import MongoDatabaseAdapter


class _CommonMongoReadRepository:

    def __init__(
        self, mongo_adapter: MongoDatabaseAdapter, collection_name: str
    ) -> None:
        self.mongo_adapter = mongo_adapter
        self.collection_name = collection_name

    async def get_by_id(self, artist_id: str) -> dict[str, Any]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
            doc["_id"] = str(doc.get("_id"))
        return doc

    async def get_by_name(self, name: str) -> dict[str, Any]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one({"name": name}, session=session)
            doc["_id"] = str(doc.get("_id"))
            return doc

    async def get_list(
        self,
        filter_obj,
    ) -> list[dict[str, Any]] | None:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            query = filter_obj.custom_filter()
            cursor = collection.find(filter=query, session=session)
            docs = []
            async for doc in cursor:
                doc["_id"] = str(doc.pop("_id"))
                docs.append(doc)
            return docs
