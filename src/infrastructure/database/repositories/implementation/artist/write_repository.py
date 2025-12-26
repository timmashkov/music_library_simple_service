from datetime import datetime

from bson import ObjectId

from domain.repositories.artist import ArtistWriteRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections


class ArtistWriteRepository(ArtistWriteRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self.mongo_adapter = mongo_adapter
        self.collection_name = Collections.ARTIST

    async def create(self, **kwargs):
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)

            result = await collection.insert_one(kwargs, session=session)
            doc = await collection.find_one(
                {"_id": result.inserted_id}, session=session
            )
            doc["_id"] = str(doc["_id"])
            return doc

    async def update(self, artist_id: str, artist: dict, updated_at: datetime):
        artist["updated_at"] = updated_at
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            await collection.update_one(
                {"_id": ObjectId(artist_id)}, {"$set": artist}, session=session
            )

            doc = await collection.find_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
            doc["_id"] = str(doc["_id"])
            return doc

    async def delete(self, artist_id: str) -> bool:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            result = await collection.delete_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
            return result.deleted_count > 0
