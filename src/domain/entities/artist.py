from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

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
