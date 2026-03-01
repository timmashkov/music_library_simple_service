from typing import Iterable
from uuid import UUID

from sqlalchemy.orm import selectinload

from domain.repositories.track import TrackReadRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Track
from infrastructure.database.repositories.common.common_read_repo import (
    _CommonReadRepository,
)


class TrackReadRepository(TrackReadRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._session = session_adapter.autocommit_session
        self._read_repo: _CommonReadRepository = _CommonReadRepository(
            session_adapter=session_adapter, model=Track, query_modifier=self.modifier
        )
        self.model = Track

    def modifier(self, query):
        query = query.options(
            selectinload(self.model.genres), selectinload(self.model.album)
        )
        return query

    async def get_by_id(self, user_id: UUID) -> Track | None:
        return await self._read_repo.get_item(user_id)

    async def search(
        self,
        filter_obj,
    ) -> Iterable[Track] | None:
        return await self._read_repo.find(filter_obj)
