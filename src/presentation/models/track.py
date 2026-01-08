from datetime import datetime

from fastapi_filter.contrib.mongoengine import Filter
from pydantic import BaseModel, Field

from application.entities.enums import TrackFormat
from infrastructure.database.models import Track
from presentation.models._common import DateTimeFieldsResponse, ResponseModelWithAliasID
from presentation.models._filter import _APIFilter


class CommandTrackModel(BaseModel):
    name: str
    duration: int
    audio_url: str | None
    bitrate: str
    format: TrackFormat


class ResponseTrackModel(
    CommandTrackModel, ResponseModelWithAliasID, DateTimeFieldsResponse
):
    pass


class TrackFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Track
