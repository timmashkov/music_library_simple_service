from enum import StrEnum

from .artist import Artist
from .album import Album


class Collections(StrEnum):
    ARTIST: str = Artist.collection_name()
    ALBUM: str = Album.collection_name()
