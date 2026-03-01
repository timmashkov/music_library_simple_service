from datetime import datetime
from uuid import UUID

from sqlalchemy import insert

from domain.entities.album import CreateAlbumDomainModel
from domain.repositories.album import AlbumWriteRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Album, AlbumGenre
from infrastructure.database.repositories.common.common_write_repo import (
    _CommonWriteRepository,
)


class AlbumWriteRepository(AlbumWriteRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._write_repo: _CommonWriteRepository = _CommonWriteRepository(
            session_adapter=session_adapter, model=Album
        )
        self._session = session_adapter

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

    async def add_genre(self, genre_uuid: UUID, track_uuid: UUID) -> AlbumGenre:
        async with self._session.transactional_session() as session:
            query = (
                insert(AlbumGenre)
                .values(genre_uuid=genre_uuid, album_uuid=track_uuid)
                .returning(AlbumGenre)
            )
            answer = await session.execute(query)
            await session.commit()
        return answer.unique().scalar_one_or_none()
