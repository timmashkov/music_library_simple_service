from dataclasses import dataclass
from datetime import datetime

from application.entities.enums import TrackFormat
from domain.entities.base import BaseDomainModel


@dataclass
class CommandTrackDomainModel(BaseDomainModel):
    duration: int
    audio_url: str | None
    bitrate: str
    format: TrackFormat


@dataclass
class ResponseTrackDomainModel(CommandTrackDomainModel):
    _id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
