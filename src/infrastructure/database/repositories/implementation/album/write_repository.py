from datetime import datetime
from uuid import UUID

from domain.entities.album import CreateAlbumDomainModel
from domain.repositories.album import AlbumWriteRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Album
from infrastructure.database.repositories.common.common_write_repo import (
    _CommonWriteRepository,
)


class AlbumWriteRepository(AlbumWriteRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._write_repo: _CommonWriteRepository = _CommonWriteRepository(
            session_adapter=session_adapter, model=Album
        )

    async def create(self, user_data: CreateAlbumDomainModel) -> Album:
        return await self._write_repo.create_item(**user_data.as_dict())

    async def update(
        self,
        artist_id: UUID,
        artist: CreateAlbumDomainModel,
        updated_at: datetime,
    ) -> Album:
        artist_data = artist.as_dict()
        artist_data["uuid"] = artist_id
        return await self._write_repo.update_item(**artist_data)

    async def delete(self, uuid: UUID) -> Album:
        return await self._write_repo.delete_item(uuid=uuid)
