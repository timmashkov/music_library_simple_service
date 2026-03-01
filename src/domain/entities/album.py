from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from domain.entities.artist import ResponseArtistDomainModel
from domain.entities.base import BaseDomainModel

if TYPE_CHECKING:
    from domain.entities.genre import ResponseGenreDomainModel
    from domain.entities.track import ResponseTrackDomainModel


@dataclass
class CreateAlbumDomainModel(BaseDomainModel):
    cover_url: str | None = None
    description: str | None = None
    artist_uuid: UUID | None = None


@dataclass(kw_only=True)
class ResponseAlbumDomainModel(CreateAlbumDomainModel):
    genres: list["ResponseGenreDomainModel"] | None
    artist: ResponseArtistDomainModel | None
    tracks: list["ResponseTrackDomainModel"] | None
    tracks_count: int = 0
    uuid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
