from typing import List, Optional
from uuid import UUID

from bson import ObjectId
from domain.entities.artist import Artist
from domain.repositories.artist import ArtistReadRepository

from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections


class ArtistReadRepositoryImpl(ArtistReadRepository):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter):
        self.mongo_adapter = mongo_adapter
        self.collection_name = Collections.ARTIST.value

    async def get_by_id(self, artist_id: str) -> Optional[Artist]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            if ObjectId.is_valid(artist_id):
                doc = await collection.find_one(
                    {"_id": ObjectId(artist_id)}, session=session
                )
            else:
                doc = await collection.find_one(
                    {"artist_id": artist_id}, session=session
                )

            return doc

    async def get_by_name(self, name: str) -> Optional[Artist]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            doc = await collection.find_one({"name": name}, session=session)
            return doc

    async def search(self, query: str, limit: int = 20) -> List[Artist]:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            cursor = (
                collection.find(
                    {"$text": {"$search": query}}, {"score": {"$meta": "textScore"}}
                )
                .sort([("score", {"$meta": "textScore"})])
                .limit(limit)
            )

            artists = []
            async for doc in cursor:
                artists.append(doc)
            return artists

    # async def get_by_genre(self, genre: str, limit: int = 20) -> List[Artist]:
    #     async with self.mongo_adapter.open_session() as session:
    #         collection = await self.mongo_adapter.get_collection(self.collection_name)
    #         cursor = collection.find({"genres": genre}).limit(limit)
    #
    #         artists = []
    #         async for doc in cursor:
    #             artists.append(self._to_domain(doc))
    #         return artists
