from typing import Any
from uuid import UUID

from domain.entities.album import ResponseAlbumDomainModel
from domain.entities.artist import ResponseArtistDomainModel
from domain.repositories.album import AlbumReadRepositoryAbs
from domain.repositories.artist import ArtistReadRepositoryAbs


class QueryArtistUseCases:
    def __init__(self, artist_repository: ArtistReadRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_read_artists(self, filters: Any) -> list[ResponseArtistDomainModel] | None:
        return await self.artist_repository.search(filters)

    async def execute_read_artist(self, name: str) -> ResponseArtistDomainModel:
        artist = await self.artist_repository.get_by_id(name)
        return ResponseArtistDomainModel(**artist)


class QueryAlbumUseCases:
    def __init__(self, album_repository: AlbumReadRepositoryAbs) -> None:
        self.album_repository = album_repository

    async def execute_read_albums(self, filters: Any) -> list[ResponseAlbumDomainModel] | None:
        return await self.album_repository.search(filters)

    async def execute_read_album(self, name: str) -> ResponseAlbumDomainModel:
        artist = await self.album_repository.get_by_id(name)
        return ResponseAlbumDomainModel(**artist)
