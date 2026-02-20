from .database_adapter import DatabaseAdapter
from .repositories.implementation.album.read_repository import AlbumReadRepository
from .repositories.implementation.album.write_repository import AlbumWriteRepository
from .repositories.implementation.artist.read_repository import ArtistReadRepository
from .repositories.implementation.artist.write_repository import ArtistWriteRepository
from .repositories.implementation.genre.read_repository import GenreReadRepository
from .repositories.implementation.genre.write_repository import GenreWriteRepository
from .repositories.implementation.track.read_repository import TrackReadRepository
from .repositories.implementation.track.write_repository import TrackWriteRepository

__all__: tuple[str] = (
    "DatabaseAdapter",
    "ArtistWriteRepository",
    "ArtistReadRepository",
    "AlbumWriteRepository",
    "AlbumReadRepository",
    "TrackWriteRepository",
    "TrackReadRepository",
    "GenreWriteRepository",
    "GenreReadRepository",
)
