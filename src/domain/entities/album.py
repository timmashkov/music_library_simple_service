from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, List, Optional

from bson import ObjectId

from application.entities.enums import AlbumType, Genres
from domain.entities.base import BaseDomainModel


@dataclass
class CommandAlbumDomainModel(BaseDomainModel):
    type: AlbumType
    genres: list[Genres] | None = None
    cover: str = None
    release_year: int | None = None
    description: str | None = None


@dataclass
class ResponseAlbumDomainModel(CommandAlbumDomainModel):
    _id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
