from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, List, Optional

from bson import ObjectId

from application.entities.enums import ArtistType, Genres
from domain.entities.base import BaseDomainModel


@dataclass
class UpdateArtistDomainModel(BaseDomainModel):
    type: ArtistType
    genres: List[Genres]
    country: Optional[str] = None
    bio: Optional[str] = None
    images: List[str] = None
    external_ids: List[str] = None
    social_links: List[str] = None
    disbanded_year: Optional[int] = None


@dataclass
class CreateArtistDomainModel(UpdateArtistDomainModel):
    formed_year: int | None = None


@dataclass
class ResponseArtistDomainModel(CreateArtistDomainModel):
    _id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
