from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_filter import FilterDepends

from application.use_cases.command_use_caces import CommandAlbumUseCases
from application.use_cases.queries_use_caces import QueryAlbumUseCases
from presentation.models._common import ResponseStatusModel
from presentation.models.album import CommandAlbumModel, ResponseAlbumModel, AlbumFilter


class AlbumRouter:
    api_router = APIRouter(prefix="/albums", tags=["albums"])

    @staticmethod
    @api_router.get("/{name}")
    @inject
    async def get_artist(
        name: str,
        use_cases: FromDishka[QueryAlbumUseCases],
    ):
        artist = await use_cases.execute_read_album(name)
        artist._id = str(artist._id)
        return artist

    @staticmethod
    @api_router.get("/")
    @inject
    async def get_users_list(
            use_cases: FromDishka[QueryAlbumUseCases],
            filters: AlbumFilter = FilterDepends(AlbumFilter),
    ):
        return await use_cases.execute_read_albums(filters)
    @staticmethod
    @api_router.post("/")
    @inject
    async def create_artist(
        command: CommandAlbumModel,
        use_cases: FromDishka[CommandAlbumUseCases],
    ):
        artist = await use_cases.execute_create_user(**command.model_dump())
        return artist

    @staticmethod
    @api_router.patch("/{artist_id}")
    @inject
    async def update_artist(
        artist_id: str,
        command: CommandAlbumModel,
        use_cases: FromDishka[CommandAlbumUseCases],
    ):
        artist = await use_cases.execute_update_user(
            **command.model_dump(), artist_id=artist_id
        )
        return artist

    @staticmethod
    @api_router.delete("/{artist_id}", response_model=ResponseStatusModel)
    @inject
    async def update_artist(
        artist_id: str,
        use_cases: FromDishka[CommandAlbumUseCases],
    ) -> ResponseStatusModel:
        is_deleted = await use_cases.execute_delete_user(artist_id=artist_id)
        return ResponseStatusModel(status=is_deleted)
