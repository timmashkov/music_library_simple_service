from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, List, Optional

from bson import ObjectId

from application.entities.enums import AlbumType, Genres, TrackFormat
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
