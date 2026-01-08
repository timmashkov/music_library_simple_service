from typing import Any

from domain.entities.album import ResponseAlbumDomainModel
from domain.entities.artist import ResponseArtistDomainModel
from domain.entities.track import ResponseTrackDomainModel
from domain.repositories.album import AlbumReadRepositoryAbs
from domain.repositories.artist import ArtistReadRepositoryAbs
from domain.repositories.track import TrackReadRepositoryAbs


class QueryArtistUseCases:
    def __init__(self, artist_repository: ArtistReadRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_read_artists(
        self, filters: Any
    ) -> list[ResponseArtistDomainModel] | None:
        artists = await self.artist_repository.search(filters)
        return [ResponseArtistDomainModel(**artist) for artist in artists if artists]

    async def execute_read_artist(self, name: str) -> ResponseArtistDomainModel:
        artist = await self.artist_repository.get_by_name(name)
        return ResponseArtistDomainModel(**artist)


class QueryAlbumUseCases:
    def __init__(self, album_repository: AlbumReadRepositoryAbs) -> None:
        self.album_repository = album_repository

    async def execute_read_albums(
        self, filters: Any
    ) -> list[ResponseAlbumDomainModel] | None:
        return await self.album_repository.search(filters)

    async def execute_read_album(self, name: str) -> ResponseAlbumDomainModel:
        album = await self.album_repository.get_by_id(name)
        return ResponseAlbumDomainModel(**album)


class QueryTrackUseCases:
    def __init__(self, track_repository: TrackReadRepositoryAbs) -> None:
        self.track_repository = track_repository

    async def execute_read_tracks(
        self, filters: Any
    ) -> list[ResponseTrackDomainModel] | None:
        return await self.track_repository.search(filters)

    async def execute_read_track(self, name: str) -> ResponseTrackDomainModel:
        track = await self.track_repository.get_by_name(name)
        return ResponseTrackDomainModel(**track)
