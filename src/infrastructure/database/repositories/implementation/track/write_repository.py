from datetime import datetime
from typing import Any

from domain.repositories.track import TrackWriteRepositoryAbs
from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.models import Collections
from infrastructure.database.repositories.common.write_repository import (
    _CommonMongoWriteRepository,
)


class TrackWriteRepository(TrackWriteRepositoryAbs):

    def __init__(self, mongo_adapter: MongoDatabaseAdapter) -> None:
        self._repository: _CommonMongoWriteRepository = _CommonMongoWriteRepository(
            mongo_adapter=mongo_adapter,
            collection_name=Collections.TRACK,
        )
        self.mongo_adapter = mongo_adapter

    async def create(self, **kwargs) -> dict[str, Any]:
        return await self._repository.create(**kwargs)

    async def update(
        self, track_id: str, track: dict, updated_at: datetime
    ) -> dict[str, Any]:
        return await self._repository.update(
            entity_id=track_id, entity=track, updated_at=updated_at
        )

    async def delete(self, track_id: str) -> bool:
        return await self._repository.delete(entity_id=track_id)
