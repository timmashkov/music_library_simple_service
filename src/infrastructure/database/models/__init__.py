from typing import TypeVar

from ._base import Base
from .album import Album
from .artist import Artist
from .association import AlbumGenre, TrackGenre
from .genre import Genre
from .track import Track

table = TypeVar("table")


__all__: tuple[str] = (
    "Base",
    "Artist",
    "Album",
    "AlbumGenre",
    "Track",
    "TrackGenre",
    "Genre",
    "table",
)
