from enum import Enum

from .album import Album
from .artist import Artist


class Collections(Enum):
    ARTIST = Artist.collection_name
    ALBUM = Album.collection_name
