from bson import ObjectId
from domain.entities.artist import Artist
from domain.repositories.artist import ArtistWriteRepository

from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections
from infrastructure.database.models.artist import Artist as ArtistModel


class ArtistWriteRepositoryImpl(ArtistWriteRepository):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self.mongo_adapter = mongo_adapter
        self.collection_name = Collections.ARTIST.value

    async def create(self, artist: Artist) -> ArtistModel:
        model = self._to_model(artist)

        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            await collection.insert_one(
                model.model_dump(by_alias=True), session=session
            )

            return artist

    async def update(self, artist_id: str, artist: Artist) -> ArtistModel:
        model = self._to_model(artist).model_dump(by_alias=True)
        model.pop("_id")
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            await collection.update_one(
                {"_id": ObjectId(artist_id)}, {"$set": model}, session=session
            )
            return artist

    async def delete(self, artist_id: str) -> bool:
        async with self.mongo_adapter.open_session() as session:
            collection = await self.mongo_adapter.get_collection(self.collection_name)
            result = await collection.delete_one(
                {"_id": ObjectId(artist_id)}, session=session
            )
            return result.deleted_count > 0

    def _to_model(self, artist: Artist) -> ArtistModel:
        """Конвертирует доменную сущность в MongoDB модель"""
        return ArtistModel(
            name=artist.name,
            type=artist.type,
            genres=artist.genres,
            country=artist.country,
            bio=artist.bio,
            images=artist.images,
            external_ids=artist.external_ids,
            social_links=artist.social_links,
            formed_year=artist.formed_year,
            disbanded_year=artist.disbanded_year,
            created_at=artist.created_at,
            updated_at=artist.updated_at,
        )
