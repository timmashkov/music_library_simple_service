from datetime import datetime
from uuid import UUID

from domain.entities.genre import CreateGenreDomainModel
from domain.repositories.genre import GenreWriteRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Genre
from infrastructure.database.repositories.common.common_write_repo import (
    _CommonWriteRepository,
)


class GenreWriteRepository(GenreWriteRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._write_repo: _CommonWriteRepository = _CommonWriteRepository(
            session_adapter=session_adapter, model=Genre
        )

    async def create(self, user_data: CreateGenreDomainModel) -> Genre:
        print(user_data, 1111)
        return await self._write_repo.create_item(**user_data.as_dict())

    async def update(
        self, artist_id: str, artist: CreateGenreDomainModel, updated_at: datetime
    ) -> Genre:
        user_data = artist.as_dict()
        user_data["uuid"] = artist_id
        return await self._write_repo.update_item(**user_data)

    async def delete(self, uuid: UUID) -> Genre:
        return await self._write_repo.delete_item(uuid=uuid)
