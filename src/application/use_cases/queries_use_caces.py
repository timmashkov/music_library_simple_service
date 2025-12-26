from typing import Any
from uuid import UUID

from domain.entities.artist import ResponseArtistDomainModel
from domain.repositories.artist import ArtistReadRepositoryAbs


class QueryArtistUseCases:
    def __init__(self, artist_repository: ArtistReadRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_read_users(self, filters: Any):
        return await self.artist_repository.search(filters)

    async def execute_read_user(self, name: str):
        artist = await self.artist_repository.get_by_id(name)
        return ResponseArtistDomainModel(**artist)
