from typing import List, Optional
from uuid import UUID

from bson import ObjectId
from fastapi_filter.contrib.mongoengine import Filter

from domain.repositories.artist import ArtistReadRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections, Artist


class ArtistReadRepository(ArtistReadRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter):
        self.mongo_adapter = mongo_adapter
        self.collection_name = Collections.ARTIST

    async def get_by_id(self, artist_id: str):
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
        return doc

    async def get_by_name(self, name: str):
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one({"name": name}, session=session)
            return doc

    async def search(
            self,
            filter_obj,
    ) -> list:
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
