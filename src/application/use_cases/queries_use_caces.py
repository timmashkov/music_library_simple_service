from typing import Any
from uuid import UUID

from domain.entities.album import ResponseAlbumDomainModel
from domain.entities.artist import ResponseArtistDomainModel
from domain.entities.genre import ResponseGenreDomainModel
from domain.entities.track import ResponseTrackDomainModel
from domain.repositories.album import AlbumReadRepositoryAbs
from domain.repositories.artist import ArtistReadRepositoryAbs
from domain.repositories.genre import GenreReadRepositoryAbs
from domain.repositories.track import TrackReadRepositoryAbs
from infrastructure.database.models import Base


class QueryArtistUseCases:
    def __init__(self, artist_repository: ArtistReadRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_read_artists(
        self, filters: Any
    ) -> list[ResponseArtistDomainModel] | None:
        artists: list[Base] = await self.artist_repository.search(filters)
        return [
            ResponseArtistDomainModel(**artist.as_dict())
            for artist in artists
            if artists
        ]

    async def execute_read_artist(self, artist_id: UUID) -> ResponseArtistDomainModel:
        artist: Base = await self.artist_repository.get_by_id(artist_id)
        return ResponseArtistDomainModel(**artist.as_dict())


class QueryAlbumUseCases:
    def __init__(self, album_repository: AlbumReadRepositoryAbs) -> None:
        self.album_repository = album_repository

    async def execute_read_albums(
        self, filters: Any
    ) -> list[ResponseAlbumDomainModel] | None:
        albums: list[Base] = await self.album_repository.search(filters)
        return [
            ResponseAlbumDomainModel(**album.as_dict()) for album in albums if albums
        ]

    async def execute_read_album(self, album_id: UUID) -> ResponseAlbumDomainModel:
        album: Base = await self.album_repository.get_by_id(album_id)
        return ResponseAlbumDomainModel(**album.as_dict())


class QueryTrackUseCases:
    def __init__(self, track_repository: TrackReadRepositoryAbs) -> None:
        self.track_repository = track_repository

    async def execute_read_tracks(
        self, filters: Any
    ) -> list[ResponseTrackDomainModel] | None:
        tracks: list[Base] = await self.track_repository.search(filters)
        return [
            ResponseTrackDomainModel(**track.as_dict()) for track in tracks if tracks
        ]

    async def execute_read_track(self, track_id: UUID) -> ResponseTrackDomainModel:
        track: Base = await self.track_repository.get_by_id(track_id)
        return ResponseTrackDomainModel(**track.as_dict())


class QueryGenreUseCases:
    def __init__(self, genre_repository: GenreReadRepositoryAbs) -> None:
        self.genre_repository = genre_repository

    async def execute_read_tracks(
        self, filters: Any
    ) -> list[ResponseGenreDomainModel] | None:
        tracks: list[Base] = await self.genre_repository.search(filters)
        return [
            ResponseGenreDomainModel(**track.as_dict()) for track in tracks if tracks
        ]

    async def execute_read_track(self, track_id: UUID) -> ResponseGenreDomainModel:
        track: Base = await self.genre_repository.get_by_id(track_id)
        return ResponseGenreDomainModel(**track.as_dict())
