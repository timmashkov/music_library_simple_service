from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from domain.entities.base import BaseDomainModel


@dataclass
class CreateArtistDomainModel(BaseDomainModel):
    bio: Optional[str] = None
    image_url: str = None


@dataclass
class ResponseArtistDomainModel(CreateArtistDomainModel):
    uuid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
