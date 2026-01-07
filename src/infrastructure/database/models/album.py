from application.entities.enums import AlbumType, Genres
from infrastructure.database.models._base import BaseMongoModel


class Album(BaseMongoModel):
    type: AlbumType
    genres: list[Genres] | None = None
    cover: str = None
    release_year: int | None = None
    description: str | None = None
