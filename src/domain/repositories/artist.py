from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from domain.entities.base import BaseDomainModel
from presentation.models._filter import _APIFilter


class ArtistReadRepositoryAbs(ABC):

    @abstractmethod
    async def get_by_id(self, artist_id: UUID) -> Optional[Any]:
        pass

    @abstractmethod
    async def search(self, query: _APIFilter) -> List[Any]:
        pass


class ArtistWriteRepositoryAbs(ABC):

    @abstractmethod
    async def create(self, artist: BaseDomainModel) -> Any:
        pass

    @abstractmethod
    async def update(
        self, artist_id: UUID, artist: BaseDomainModel, updated_at: datetime
    ) -> Any:
        pass

    @abstractmethod
    async def delete(self, artist_id: UUID) -> bool:
        pass
