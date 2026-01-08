from typing import Any

from domain.repositories.artist import ArtistReadRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections
from infrastructure.database.repositories.common.read_repository import (
    _CommonMongoReadRepository,
)


class ArtistReadRepository(ArtistReadRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self._repository: _CommonMongoReadRepository = _CommonMongoReadRepository(
            mongo_adapter=mongo_adapter,
            collection_name=Collections.ARTIST,
        )
        self.mongo_adapter = mongo_adapter

    async def get_by_id(self, artist_id: str) -> dict[str, Any]:
        return await self._repository.get_by_id(artist_id)

    async def get_by_name(self, name: str) -> dict[str, Any]:
        return await self._repository.get_by_name(name)

    async def search(
        self,
        filter_obj,
    ) -> list[dict[str, Any]] | None:
        return await self._repository.get_list(filter_obj)
