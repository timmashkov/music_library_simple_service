from typing import Any

from domain.repositories.track import TrackReadRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections
from infrastructure.database.repositories.common.read_repository import (
    _CommonMongoReadRepository,
)


class TrackReadRepository(TrackReadRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self._repository: _CommonMongoReadRepository = _CommonMongoReadRepository(
            mongo_adapter=mongo_adapter,
            collection_name=Collections.TRACK,
        )
        self.mongo_adapter = mongo_adapter

    async def get_by_id(self, track_id: str) -> dict[str, Any]:
        return await self._repository.get_by_id(track_id)

    async def get_by_name(self, name: str) -> dict[str, Any]:
        return await self._repository.get_by_name(name)

    async def search(
        self,
        filter_obj,
    ) -> list[dict[str, Any]] | None:
        return await self._repository.get_list(filter_obj)
