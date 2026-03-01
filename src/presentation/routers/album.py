from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases.command_use_caces import CommandAlbumUseCases
from application.use_cases.queries_use_caces import QueryAlbumUseCases
from presentation.models._common import AddGenreModel, ResponseStatusModel
from presentation.models.album import AlbumFilter, CommandAlbumModel, ResponseAlbumModel
from presentation.routers import BaseRouter


class AlbumRouter(BaseRouter):
    api_router = APIRouter(prefix="/albums", tags=["albums"])
    input_model = CommandAlbumModel
    output_model = ResponseAlbumModel

    @staticmethod
    @api_router.get("/{name}", response_model=output_model)
    @inject
    async def get_album(
        name: str,
        use_cases: FromDishka[QueryAlbumUseCases],
    ):
        return await use_cases.execute_read_album(name)

    @staticmethod
    @api_router.get("/", response_model=list[output_model])
    @inject
    async def get_albums_list(
        use_cases: FromDishka[QueryAlbumUseCases],
        filters: AlbumFilter = FilterDepends(AlbumFilter),
    ):
        lst = await use_cases.execute_read_albums(filters)
        print(lst)
        return lst

    @staticmethod
    @api_router.post("/{domain_uuid}/genres", response_model=None)
    @inject
    async def add_genre_to_albim(
        use_cases: FromDishka[CommandAlbumUseCases],
        domain_uuid: UUID,
        data: AddGenreModel,
    ):
        data.domain_uuid = domain_uuid
        return await use_cases.execute_add_track(data)

    @staticmethod
    @api_router.post("/")
    @inject
    async def create_album(
        command: CommandAlbumModel,
        use_cases: FromDishka[CommandAlbumUseCases],
    ):
        return await use_cases.execute_create_album(**command.model_dump())

    @staticmethod
    @api_router.patch("/{album_id}")
    @inject
    async def update_album(
        album_id: str,
        command: CommandAlbumModel,
        use_cases: FromDishka[CommandAlbumUseCases],
    ):
        return await use_cases.execute_update_album(
            **command.model_dump(), album_id=album_id
        )

    @staticmethod
    @api_router.delete("/{artist_id}", response_model=ResponseStatusModel)
    @inject
    async def delete_album(
        artist_id: str,
        use_cases: FromDishka[CommandAlbumUseCases],
    ) -> ResponseStatusModel:
        is_deleted = await use_cases.execute_delete_album(artist_id=artist_id)
        return ResponseStatusModel(status=is_deleted)
