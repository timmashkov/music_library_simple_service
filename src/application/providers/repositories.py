from dishka import Provider, Scope, provide

from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.repositories.implementation.artist.read_repository import (
    ArtistReadRepository,
)
from infrastructure.database.repositories.implementation.artist.write_repository import (
    ArtistWriteRepository,
)
from infrastructure.database.repositories.implementation.album.read_repository import (
    AlbumReadRepository,
)
from infrastructure.database.repositories.implementation.album.write_repository import (
    AlbumWriteRepository,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_artist_read_repo(
        self, mongo_adapter: MongoDatabaseAdapter
    ) -> ArtistReadRepository:
        return ArtistReadRepository(mongo_adapter)

    @provide(scope=Scope.REQUEST)
    def get_artist_write_repo(
        self, mongo_adapter: MongoDatabaseAdapter
    ) -> ArtistWriteRepository:
        return ArtistWriteRepository(mongo_adapter)

    @provide(scope=Scope.REQUEST)
    def get_album_read_repo(
            self, mongo_adapter: MongoDatabaseAdapter
    ) -> AlbumReadRepository:
        return AlbumReadRepository(mongo_adapter)

    @provide(scope=Scope.REQUEST)
    def get_album_write_repo(
            self, mongo_adapter: MongoDatabaseAdapter
    ) -> AlbumWriteRepository:
        return AlbumWriteRepository(mongo_adapter)
