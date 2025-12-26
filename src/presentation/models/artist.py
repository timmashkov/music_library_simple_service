from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field

from application.entities.enums import ArtistType, Genres


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


class ResponseArtistDomainModel(CreateArtistModel):
    created_at: datetime
    updated_at: datetime
