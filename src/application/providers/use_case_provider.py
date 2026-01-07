from dishka import Provider, Scope, provide

from application.use_cases.command_use_caces import CommandArtistUseCases, CommandAlbumUseCases, CommandTrackUseCases
from application.use_cases.queries_use_caces import QueryArtistUseCases, QueryAlbumUseCases, QueryTrackUseCases
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
from infrastructure.database.repositories.implementation.track.read_repository import (
    TrackReadRepository,
)
from infrastructure.database.repositories.implementation.track.write_repository import (
    TrackWriteRepository,
)


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_query_artist_use_cases(
        self, _repository: ArtistReadRepository
    ) -> QueryArtistUseCases:
        return QueryArtistUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_command_artist_use_cases(
        self, _repository: ArtistWriteRepository
    ) -> CommandArtistUseCases:
        return CommandArtistUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_query_album_use_cases(
            self, _repository: AlbumReadRepository
    ) -> QueryAlbumUseCases:
        return QueryAlbumUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_command_album_use_cases(
            self, _repository: AlbumWriteRepository
    ) -> CommandAlbumUseCases:
        return CommandAlbumUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_query_track_use_cases(
            self, _repository: TrackReadRepository
    ) -> QueryTrackUseCases:
        return QueryTrackUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_command_track_use_cases(
            self, _repository: TrackWriteRepository
    ) -> CommandTrackUseCases:
        return CommandTrackUseCases(_repository)
