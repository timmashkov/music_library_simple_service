from typing import Iterable
from uuid import UUID

from domain.repositories.genre import GenreReadRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Genre
from infrastructure.database.repositories.common.common_read_repo import (
    _CommonReadRepository,
)


class GenreReadRepository(GenreReadRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._session = session_adapter.autocommit_session
        self._read_repo: _CommonReadRepository = _CommonReadRepository(
            session_adapter=session_adapter, model=Genre
        )

    async def get_by_id(self, user_id: UUID) -> Genre | None:
        return await self._read_repo.get_item(user_id)

    async def search(
        self,
        filter_obj,
    ) -> Iterable[Genre] | None:
        return await self._read_repo.find(filter_obj)
