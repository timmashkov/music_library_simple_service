from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, List, Optional

from fastapi_filter.contrib.mongoengine import Filter
from pydantic import BaseModel, Field

from application.entities.enums import ArtistType, Genres, AlbumType
from infrastructure.database.models import Artist, Album
from presentation.models._filter import _APIFilter


class CommandAlbumModel(BaseModel):
    name: str
    type: AlbumType
    genres: list[Genres] | None = None
    cover: str = None
    release_year: int | None = None
    description: str | None = None


class ResponseAlbumModel(CommandAlbumModel):
    id: str
    created_at: datetime
    updated_at: datetime


class AlbumFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Album
