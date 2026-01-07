from enum import StrEnum

from .artist import Artist
from .album import Album
from .track import Track


class Collections(StrEnum):
    ARTIST: str = Artist.collection_name()
    ALBUM: str = Album.collection_name()
    TRACK: str = Track.collection_name()
