from typing import Iterable
from uuid import UUID

from domain.repositories.album import AlbumReadRepositoryAbs
from infrastructure.database.database_adapter import DatabaseAdapter
from infrastructure.database.models import Album
from infrastructure.database.repositories.common.common_read_repo import (
    _CommonReadRepository,
)


class AlbumReadRepository(AlbumReadRepositoryAbs):

    def __init__(self, session_adapter: DatabaseAdapter) -> None:
        self._session = session_adapter.autocommit_session
        self._read_repo: _CommonReadRepository = _CommonReadRepository(
            session_adapter=session_adapter, model=Album
        )

    async def get_by_id(self, user_id: UUID) -> Album | None:
        return await self._read_repo.get_item(user_id)

    async def search(
        self,
        filter_obj,
    ) -> Iterable[Album] | None:
        return await self._read_repo.find(filter_obj)
