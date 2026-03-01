from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from domain.entities.base import BaseDomainModel


class AlbumReadRepositoryAbs(ABC):

    @abstractmethod
    async def get_by_id(self, album_id: UUID) -> Optional[Any]:
        pass

    @abstractmethod
    async def search(self, query: Any) -> List[Any]:
        pass


class AlbumWriteRepositoryAbs(ABC):

    @abstractmethod
    async def create(self, album: BaseDomainModel) -> Any:
        pass

    @abstractmethod
    async def add_genre(self, genre_uuid: UUID, track_uuid: UUID) -> Any:
        pass

    @abstractmethod
    async def update(
        self, album_id: UUID, album: BaseDomainModel, updated_at: datetime
    ) -> Any:
        pass

    @abstractmethod
    async def delete(self, album_id: UUID) -> bool:
        pass
