from datetime import datetime
from uuid import UUID

from domain.entities.artist import CreateArtistDomainModel
from domain.repositories.artist import ArtistWriteRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Artist
from infrastructure.database.repositories.common.common_write_repo import (
    _CommonWriteRepository,
)


class ArtistWriteRepository(ArtistWriteRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._write_repo: _CommonWriteRepository = _CommonWriteRepository(
            session_adapter=session_adapter, model=Artist
        )

    async def create(self, user_data: CreateArtistDomainModel) -> Artist:
        return await self._write_repo.create_item(**user_data.as_dict())

    async def update(
        self,
        artist_id: UUID,
        artist: CreateArtistDomainModel,
        updated_at: datetime,
    ) -> Artist:
        user_data = artist.as_dict()
        user_data["uuid"] = artist_id
        return await self._write_repo.update_item(**user_data)

    async def delete(self, uuid: UUID) -> Artist:
        return await self._write_repo.delete_item(uuid=uuid)
