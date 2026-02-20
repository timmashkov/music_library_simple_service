from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from application.entities.enums import TrackFormat
from domain.entities.base import BaseDomainModel


@dataclass
class CreateTrackDomainModel(BaseDomainModel):
    duration: int | None = None
    audio_url: str | None = None
    bitrate: str | None = None
    format: TrackFormat | None = None
    artist_uuid: UUID = None
    album_uuid: UUID = None


@dataclass
class ResponseTrackDomainModel(CreateTrackDomainModel):
    _id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
