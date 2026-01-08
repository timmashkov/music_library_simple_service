from datetime import datetime
from typing import List, Optional

from fastapi_filter.contrib.mongoengine import Filter
from pydantic import BaseModel, Field

from application.entities.enums import ArtistType, Genres
from infrastructure.database.models import Artist
from presentation.models._common import DateTimeFieldsResponse, ResponseModelWithAliasID
from presentation.models._filter import _APIFilter


class UpdateArtistModel(BaseModel):
    name: str
    type: ArtistType
    genres: List[Genres]
    country: Optional[str] = None
    bio: Optional[str] = None
    images: List[str] = None
    external_ids: List[str] = None
    social_links: List[str] = None
    disbanded_year: Optional[int] = None


class CreateArtistModel(UpdateArtistModel):
    formed_year: int | None = None


class ResponseArtistModel(
    CreateArtistModel, ResponseModelWithAliasID, DateTimeFieldsResponse
):
    pass


class ArtistFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Artist
