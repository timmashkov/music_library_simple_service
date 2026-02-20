from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases.command_use_caces import CommandGenreUseCases
from application.use_cases.queries_use_caces import QueryGenreUseCases
from presentation.models._common import ResponseStatusModel
from presentation.models.genre import GenreCreateModel, GenreFilter, ResponseGenreModel
from presentation.routers import BaseRouter


class GenreRouter(BaseRouter):
    api_router = APIRouter(prefix="/genres", tags=["Genres"])
    input_model = GenreCreateModel
    output_model = ResponseGenreModel

    @staticmethod
    @api_router.get("/{genre_id}", response_model=output_model)
    @inject
    async def get_track(
        genre_id: UUID,
        use_cases: FromDishka[QueryGenreUseCases],
    ):
        return await use_cases.execute_read_track(genre_id)

    @staticmethod
    @api_router.get("/", response_model=list[output_model])
    @inject
    async def get_tracks_list(
        use_cases: FromDishka[QueryGenreUseCases],
        filters: GenreFilter = FilterDepends(GenreFilter),
    ):
        return await use_cases.execute_read_tracks(filters)

    @staticmethod
    @api_router.post("/", response_model=output_model)
    @inject
    async def create_track(
        command: input_model,
        use_cases: FromDishka[CommandGenreUseCases],
    ):
        return await use_cases.execute_create_track(**command.model_dump())

    @staticmethod
    @api_router.patch("/{genre_id}", response_model=output_model)
    @inject
    async def update_track(
        genre_id: UUID,
        command: input_model,
        use_cases: FromDishka[CommandGenreUseCases],
    ):
        return await use_cases.execute_update_track(
            **command.model_dump(), artist_id=genre_id
        )

    @staticmethod
    @api_router.delete("/{genre_id}", response_model=ResponseStatusModel)
    @inject
    async def delete_track(
        genre_id: UUID,
        use_cases: FromDishka[CommandGenreUseCases],
    ) -> ResponseStatusModel:
        is_deleted = await use_cases.execute_delete_track(artist_id=genre_id)
        return ResponseStatusModel(status=is_deleted)
