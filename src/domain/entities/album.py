from dataclasses import dataclass
from datetime import datetime

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
