from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel, Field

from infrastructure.database.models import Genre
from presentation.models._common import DateTimeFieldsResponse, UUIDResponse
from presentation.models._filter import _APIFilter


class GenreCreateModel(BaseModel):
    name: str = None
    data: dict = None


class ResponseGenreModel(GenreCreateModel, UUIDResponse, DateTimeFieldsResponse):
    pass


class GenreFilter(_APIFilter):

    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sorted_by: list[str] = Field(default=["created_at"])

    class Constants(Filter.Constants):
        model = Genre
