from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from domain.entities.base import BaseDomainModel
from presentation.models._filter import _APIFilter


class TrackReadRepositoryAbs(ABC):

    @abstractmethod
    async def get_by_id(self, track_id: UUID) -> Optional[Any]:
        pass

    @abstractmethod
    async def search(self, query: _APIFilter) -> List[Any]:
        pass


class TrackWriteRepositoryAbs(ABC):

    @abstractmethod
    async def create(self, track: BaseDomainModel) -> Any:
        pass

    @abstractmethod
    async def update(
        self, track_id: UUID, track: BaseDomainModel, updated_at: datetime
    ) -> Any:
        pass

    @abstractmethod
    async def delete(self, track_id: UUID) -> bool:
        pass
