from datetime import datetime
from uuid import UUID

from sqlalchemy import insert

from domain.entities.artist import CreateArtistDomainModel
from domain.repositories.track import TrackWriteRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Track, TrackGenre
from infrastructure.database.repositories.common.common_write_repo import (
    _CommonWriteRepository,
)


class TrackWriteRepository(TrackWriteRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._write_repo: _CommonWriteRepository = _CommonWriteRepository(
            session_adapter=session_adapter, model=Track
        )
        self._session = session_adapter

    async def create(self, user_data: CreateArtistDomainModel) -> Track:
        return await self._write_repo.create_item(**user_data.as_dict())

    async def update(
        self, artist_id: str, artist: CreateArtistDomainModel, updated_at: datetime
    ) -> Track:
        user_data = artist.as_dict()
        user_data["uuid"] = artist_id
        return await self._write_repo.update_item(**user_data)

    async def delete(self, uuid: UUID) -> Track:
        return await self._write_repo.delete_item(uuid=uuid)

    async def add_genre(self, genre_uuid: UUID, track_uuid: UUID) -> TrackGenre:
        async with self._session.transactional_session() as session:
            query = (
                insert(TrackGenre)
                .values(genre_uuid=genre_uuid, track_uuid=track_uuid)
                .returning(TrackGenre)
            )
            answer = await session.execute(query)
            await session.commit()
        return answer.unique().scalar_one_or_none()
