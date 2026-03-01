from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ResponseStatusModel(BaseModel):
    status: bool


class DateTimeFieldsResponse(BaseModel):
    created_at: datetime | None
    updated_at: datetime | None


class UUIDResponse(BaseModel):
    uuid: UUID


class AddGenreModel(BaseModel):
    genre_uuid: UUID
    domain_uuid: UUID | None = None
