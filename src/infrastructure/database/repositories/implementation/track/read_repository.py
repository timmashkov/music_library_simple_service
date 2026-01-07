from typing import Any

from bson import ObjectId

from domain.repositories.track import TrackReadRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections


class TrackReadRepository(TrackReadRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self.mongo_adapter = mongo_adapter
        self.collection_name = Collections.TRACK

    async def get_by_id(self, artist_id: str) -> dict[str, Any]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
        return doc

    async def get_by_name(self, name: str) -> dict[str, Any]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one({"name": name}, session=session)
            return doc

    async def search(
            self,
            filter_obj,
    ) -> list[dict[str, Any]] | None:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            query = filter_obj.custom_filter()
            cursor = collection.find(
                filter=query,
                session=session
            )
            docs = []
            async for doc in cursor:
                doc['_id'] = str(doc.pop('_id'))
                docs.append(doc)
            return docs
