from dishka import Provider, Scope, provide

from infrastructure.database.database_adapter import MongoDatabaseAdapter
from infrastructure.database.repositories.implementation.artist.read_repository import (
    ArtistReadRepository,
)
from infrastructure.database.repositories.implementation.artist.write_repository import (
    ArtistWriteRepository,
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
