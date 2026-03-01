from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from domain.entities.base import BaseDomainModel

if TYPE_CHECKING:
    from domain.entities.album import ResponseAlbumDomainModel


@dataclass
class CreateArtistDomainModel(BaseDomainModel):
    bio: str = None
    image_url: str = None


@dataclass(kw_only=True)
class ResponseArtistDomainModel(CreateArtistDomainModel):
    albums: list["ResponseAlbumDomainModel"] | None
    albums_count: int | None
    uuid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
