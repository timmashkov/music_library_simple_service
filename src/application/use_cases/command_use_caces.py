from datetime import datetime, timezone
from uuid import UUID

from bson import ObjectId

from domain.entities.artist import (
    CreateArtistDomainModel,
    ResponseArtistDomainModel,
    UpdateArtistDomainModel,
)
from domain.repositories.artist import ArtistWriteRepositoryAbs


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
