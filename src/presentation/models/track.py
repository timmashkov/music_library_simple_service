from datetime import datetime
from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, Field

from application.entities.enums import TrackFormat
from infrastructure.database.models import Track
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter


class CommandTrackModel(BaseModel):
    name: str
    duration: int
    audio_url: str | None
    bitrate: str
    artist_uuid: UUID
    album_uuid: UUID
    format: TrackFormat


class ResponseTrackModel(CommandTrackModel, UUIDResponse, DateTimeFieldsResponse):
    pass


class TrackFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Track
