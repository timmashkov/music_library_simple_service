from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, ConfigDict, Field

from application.entities.enums import TrackFormat
from infrastructure.database.models import Track
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter
from presentation.models.genre import ResponseGenreModel

if TYPE_CHECKING:
    from presentation.models.album import ResponseAlbumModel


class CommandTrackModel(BaseModel):
    name: str
    duration: int
    audio_url: str | None
    bitrate: str
    artist_uuid: UUID
    album_uuid: UUID
    format: TrackFormat


class ResponseTrackModel(CommandTrackModel, UUIDResponse, DateTimeFieldsResponse):
    genres: list[ResponseGenreModel]
    album: "ResponseAlbumModel"
    model_config = ConfigDict(from_attributes=True)


class TrackFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Track
