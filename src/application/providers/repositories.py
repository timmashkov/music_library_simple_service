from dishka import Provider, Scope, provide

from infrastructure.database import (
    AlbumReadRepository,
    AlbumWriteRepository,
    ArtistReadRepository,
    ArtistWriteRepository,
    DatabaseAdapter,
    TrackReadRepository,
    TrackWriteRepository,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_artist_read_repo(
        self, session_adapter: DatabaseAdapter
    ) -> ArtistReadRepository:
        return ArtistReadRepository(session_adapter)

    @provide(scope=Scope.REQUEST)
    def get_artist_write_repo(
        self, session_adapter: DatabaseAdapter
    ) -> ArtistWriteRepository:
        return ArtistWriteRepository(session_adapter)

    @provide(scope=Scope.REQUEST)
    def get_album_read_repo(
        self, session_adapter: DatabaseAdapter
    ) -> AlbumReadRepository:
        return AlbumReadRepository(session_adapter)

    @provide(scope=Scope.REQUEST)
    def get_album_write_repo(
        self, session_adapter: DatabaseAdapter
    ) -> AlbumWriteRepository:
        return AlbumWriteRepository(session_adapter)

    @provide(scope=Scope.REQUEST)
    def get_track_read_repo(
        self, session_adapter: DatabaseAdapter
    ) -> TrackReadRepository:
        return TrackReadRepository(session_adapter)

    @provide(scope=Scope.REQUEST)
    def get_track_write_repo(
        self, session_adapter: DatabaseAdapter
    ) -> TrackWriteRepository:
        return TrackWriteRepository(session_adapter)
