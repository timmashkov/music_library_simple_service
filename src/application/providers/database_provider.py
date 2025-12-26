from dishka import Provider, Scope, provide

from application.config import settings
from infrastructure.database.database_adapter import MongoDatabaseAdapter


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_db_adapter(self) -> MongoDatabaseAdapter:
        return MongoDatabaseAdapter(
            host=settings.MONGODB.host,
            port=settings.MONGODB.port,
            user=settings.MONGODB.user,
            password=settings.MONGODB.password,
            database_name=settings.MONGODB.database,
        )
