from typing import Iterable
from uuid import UUID

from sqlalchemy.orm import selectinload

from domain.repositories.artist import ArtistReadRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Artist
from infrastructure.database.repositories.common.common_read_repo import (
    _CommonReadRepository,
)


class ArtistReadRepository(ArtistReadRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._session = session_adapter.autocommit_session
        self._read_repo: _CommonReadRepository = _CommonReadRepository(
            session_adapter=session_adapter, model=Artist, query_modifier=self.modifier
        )
        self.model = Artist

    def modifier(self, query):
        query = query.options(selectinload(self.model.albums))
        return query

    async def get_by_id(self, user_id: UUID) -> Artist | None:
        return await self._read_repo.get_item(user_id)

    async def search(
        self,
        filter_obj,
    ) -> Iterable[Artist] | None:
        return await self._read_repo.find(filter_obj)
