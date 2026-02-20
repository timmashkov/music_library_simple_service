from datetime import datetime
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, Field

from infrastructure.database.models import Artist
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter


class CreateArtistModel(BaseModel):
    name: str
    data: dict = None
    bio: Optional[str] = None
    image_url: str = None


class ResponseArtistModel(CreateArtistModel, DateTimeFieldsResponse, UUIDResponse):
    pass


class ArtistFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Artist
