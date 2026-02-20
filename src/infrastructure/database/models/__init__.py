from typing import TypeVar

from ._base import Base
from .album import Album
from .artist import Artist
from .track import Track

table = TypeVar("table")


__all__: tuple[str] = (
    "Base",
    "Artist",
    "Album",
    "Track",
    "table",
)
