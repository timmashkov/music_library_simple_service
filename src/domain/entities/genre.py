from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.entities.base import BaseDomainModel


@dataclass
class CreateGenreDomainModel(BaseDomainModel):
    description: str | None = None


@dataclass
class ResponseGenreDomainModel(CreateGenreDomainModel):
    uuid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
