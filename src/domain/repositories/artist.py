from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Optional


class ArtistReadRepositoryAbs(ABC):

    @abstractmethod
    async def get_by_id(self, artist_id: str) -> Optional[Any]:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[Any]:
        pass

    @abstractmethod
    async def search(self, query: str, limit: int = 20) -> List[Any]:
        pass

    # @abstractmethod
    # async def get_by_genre(self, genre: str, limit: int = 20) -> List[Any]:
    #     pass


class ArtistWriteRepositoryAbs(ABC):

    @abstractmethod
    async def create(self, artist: Any) -> Any:
        pass

    @abstractmethod
    async def update(self, artist_id: str, artist: Any, updated_at: datetime) -> Any:
        pass

    @abstractmethod
    async def delete(self, artist_id: str) -> bool:
        pass
