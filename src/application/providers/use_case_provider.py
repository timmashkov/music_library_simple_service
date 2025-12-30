from dishka import Provider, Scope, provide

from application.use_cases.command_use_caces import CommandArtistUseCases
from application.use_cases.queries_use_caces import QueryArtistUseCases
from infrastructure.database.repositories.implementation.artist.read_repository import (
    ArtistReadRepository,
)
from infrastructure.database.repositories.implementation.artist.write_repository import (
    ArtistWriteRepository,
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
