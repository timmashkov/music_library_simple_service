from datetime import datetime
from uuid import UUID

from domain.entities.album import CreateAlbumDomainModel, ResponseAlbumDomainModel
from domain.entities.artist import CreateArtistDomainModel, ResponseArtistDomainModel
from domain.entities.genre import CreateGenreDomainModel, ResponseGenreDomainModel
from domain.entities.track import CreateTrackDomainModel, ResponseTrackDomainModel
from domain.repositories.album import AlbumWriteRepositoryAbs
from domain.repositories.artist import ArtistWriteRepositoryAbs
from domain.repositories.genre import GenreWriteRepositoryAbs
from domain.repositories.track import TrackWriteRepositoryAbs


class CommandArtistUseCases:
    def __init__(self, artist_repository: ArtistWriteRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_create_artist(self, **kwargs) -> ResponseArtistDomainModel:
        command = CreateArtistDomainModel(**kwargs)
        return await self.artist_repository.create(command)

    async def execute_update_artist(self, **kwargs) -> ResponseArtistDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = CreateArtistDomainModel(**kwargs)
        return await self.artist_repository.update(
            artist_id, command, updated_at=datetime.now()
        )

    async def execute_delete_artist(self, artist_id: UUID) -> bool:
        return await self.artist_repository.delete(artist_id)


class CommandAlbumUseCases:
    def __init__(self, album_repository: AlbumWriteRepositoryAbs) -> None:
        self.album_repository = album_repository

    async def execute_create_album(self, **kwargs) -> ResponseAlbumDomainModel:
        command = CreateAlbumDomainModel(**kwargs)
        return await self.album_repository.create(command)

    async def execute_update_album(self, **kwargs) -> ResponseAlbumDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = CreateAlbumDomainModel(**kwargs)
        return await self.album_repository.update(
            artist_id, command, updated_at=datetime.now()
        )

    async def execute_delete_album(self, artist_id: UUID) -> bool:
        return await self.album_repository.delete(artist_id)


class CommandTrackUseCases:
    def __init__(self, track_repository: TrackWriteRepositoryAbs) -> None:
        self.track_repository = track_repository

    async def execute_create_track(self, **kwargs) -> ResponseTrackDomainModel:
        command = CreateTrackDomainModel(**kwargs)
        return await self.track_repository.create(command)

    async def execute_update_track(self, **kwargs) -> ResponseTrackDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = CreateTrackDomainModel(**kwargs)
        return await self.track_repository.update(
            artist_id, command, updated_at=datetime.now()
        )

    async def execute_delete_track(self, artist_id: UUID) -> bool:
        return await self.track_repository.delete(artist_id)


class CommandGenreUseCases:
    def __init__(self, genre_repository: GenreWriteRepositoryAbs) -> None:
        self.genre_repository = genre_repository

    async def execute_create_track(self, **kwargs) -> ResponseGenreDomainModel:
        command = CreateGenreDomainModel(**kwargs)
        return await self.genre_repository.create(command)

    async def execute_update_track(self, **kwargs) -> ResponseGenreDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = CreateGenreDomainModel(**kwargs)
        return await self.genre_repository.update(
            artist_id, command, updated_at=datetime.now()
        )

    async def execute_delete_track(self, artist_id: UUID) -> bool:
        return await self.genre_repository.delete(artist_id)
