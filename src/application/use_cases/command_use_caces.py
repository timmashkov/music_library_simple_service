from datetime import datetime, timezone
from uuid import UUID

from bson import ObjectId

from domain.entities.artist import (
    CreateArtistDomainModel,
    ResponseArtistDomainModel,
    UpdateArtistDomainModel,
)
from domain.entities.album import (
    CommandAlbumDomainModel,
    ResponseAlbumDomainModel,
)
from domain.entities.track import ResponseTrackDomainModel, CommandTrackDomainModel
from domain.repositories.album import AlbumWriteRepositoryAbs
from domain.repositories.artist import ArtistWriteRepositoryAbs
from domain.repositories.track import TrackWriteRepositoryAbs


class CommandArtistUseCases:
    def __init__(self, artist_repository: ArtistWriteRepositoryAbs) -> None:
        self.artist_repository = artist_repository

    async def execute_create_user(self, **kwargs) -> ResponseArtistDomainModel:
        command = CreateArtistDomainModel(**kwargs)
        inserted_doc = await self.artist_repository.create(
            **command.as_dict(), created_at=datetime.now(timezone.utc)
        )
        return ResponseArtistDomainModel(**inserted_doc)

    async def execute_update_user(self, **kwargs) -> ResponseArtistDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = UpdateArtistDomainModel(**kwargs)
        updated_doc = await self.artist_repository.update(
            artist_id=artist_id,
            artist=command.as_dict(),
            updated_at=datetime.now(timezone.utc),
        )
        return ResponseArtistDomainModel(**updated_doc)

    async def execute_delete_user(self, artist_id: str) -> bool:
        return await self.artist_repository.delete(artist_id)


class CommandAlbumUseCases:
    def __init__(self, artist_repository: AlbumWriteRepositoryAbs) -> None:
        self.album_repository = artist_repository

    async def execute_create_user(self, **kwargs) -> ResponseAlbumDomainModel:
        command = CommandAlbumDomainModel(**kwargs)
        inserted_doc = await self.album_repository.create(
            **command.as_dict(), created_at=datetime.now(timezone.utc)
        )
        return ResponseAlbumDomainModel(**inserted_doc)

    async def execute_update_user(self, **kwargs) -> ResponseAlbumDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = UpdateArtistDomainModel(**kwargs)
        updated_doc = await self.album_repository.update(
            artist_id=artist_id,
            artist=command.as_dict(),
            updated_at=datetime.now(timezone.utc),
        )
        return ResponseAlbumDomainModel(**updated_doc)

    async def execute_delete_user(self, artist_id: str) -> bool:
        return await self.album_repository.delete(artist_id)


class CommandTrackUseCases:
    def __init__(self, track_repository: TrackWriteRepositoryAbs) -> None:
        self.track_repository = track_repository

    async def execute_create_track(self, **kwargs) -> ResponseTrackDomainModel:
        command = CommandTrackDomainModel(**kwargs)
        inserted_doc = await self.track_repository.create(
            **command.as_dict(), created_at=datetime.now(timezone.utc)
        )
        return ResponseTrackDomainModel(**inserted_doc)

    async def execute_update_track(self, **kwargs) -> ResponseTrackDomainModel:
        artist_id = kwargs.pop("artist_id")
        command = CommandTrackDomainModel(**kwargs)
        updated_doc = await self.track_repository.update(
            artist_id=artist_id,
            artist=command.as_dict(),
            updated_at=datetime.now(timezone.utc),
        )
        return ResponseTrackDomainModel(**updated_doc)

    async def execute_delete_track(self, artist_id: str) -> bool:
        return await self.track_repository.delete(artist_id)
