from application.entities.enums import ArtistType, Genres
from infrastructure.database.models._base import BaseMongoModel


class Artist(BaseMongoModel):
    type: ArtistType
    genres: list[Genres] | None = None
    country: str | None = None
    bio: str | None = None
    images: list[str] = None
    social_links: list[str] = None
    formed_year: int | None = None
    disbanded_year: int | None = None
