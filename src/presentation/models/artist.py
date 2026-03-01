from datetime import datetime
from typing import TYPE_CHECKING, Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, ConfigDict, Field

from infrastructure.database.models import Artist
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter

if TYPE_CHECKING:
    from .album import ResponseAlbumModel


class CreateArtistModel(BaseModel):
    name: str
    data: dict = None
    bio: Optional[str] = None
    image_url: str = None


class ResponseArtistModel(CreateArtistModel, DateTimeFieldsResponse, UUIDResponse):
    albums: list["ResponseAlbumModel"] | None
    albums_count: int | None
    model_config = ConfigDict(from_attributes=True)


class ArtistFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Artist
