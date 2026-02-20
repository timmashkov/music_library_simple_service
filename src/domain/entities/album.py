from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


from domain.entities.base import BaseDomainModel


@dataclass
class CreateAlbumDomainModel(BaseDomainModel):
    cover_url: str | None = None
    description: str | None = None
    artist_uuid: UUID | None = None


@dataclass
class ResponseAlbumDomainModel(CreateAlbumDomainModel):
    uuid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
