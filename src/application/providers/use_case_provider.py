from dishka import Provider, Scope, provide

from application.use_cases.command_use_caces import (
    CommandAlbumUseCases,
    CommandArtistUseCases,
    CommandGenreUseCases,
    CommandTrackUseCases,
)
from application.use_cases.queries_use_caces import (
    QueryAlbumUseCases,
    QueryArtistUseCases,
    QueryGenreUseCases,
    QueryTrackUseCases,
)
from infrastructure.database import (
    AlbumReadRepository,
    AlbumWriteRepository,
    ArtistReadRepository,
    ArtistWriteRepository,
    GenreReadRepository,
    GenreWriteRepository,
    TrackReadRepository,
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

    @provide(scope=Scope.REQUEST)
    def provide_query_genre_use_cases(
        self, _repository: GenreReadRepository
    ) -> QueryGenreUseCases:
        return QueryGenreUseCases(_repository)

    @provide(scope=Scope.REQUEST)
    def provide_command_genre_use_cases(
        self, _repository: GenreWriteRepository
    ) -> CommandGenreUseCases:
        return CommandGenreUseCases(_repository)
