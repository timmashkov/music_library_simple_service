from datetime import datetime
from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, Field

from infrastructure.database.models import Album
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter


class CommandAlbumModel(BaseModel):
    name: str = None
    data: dict = None
    cover_url: str | None = None
    description: str | None = None
    artist_uuid: UUID | None = None


class ResponseAlbumModel(CommandAlbumModel, UUIDResponse, DateTimeFieldsResponse):
    pass


class AlbumFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Album
