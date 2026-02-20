from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases.command_use_caces import CommandArtistUseCases
from application.use_cases.queries_use_caces import QueryArtistUseCases
from presentation.models._common import ResponseStatusModel
from presentation.models.artist import (
    ArtistFilter,
    CreateArtistModel,
    ResponseArtistModel,
)
from presentation.routers import BaseRouter


class ArtistRouter(BaseRouter):
    api_router = APIRouter(prefix="/artists", tags=["artists"])
    input_model = CreateArtistModel
    output_model = ResponseArtistModel

    @staticmethod
    @api_router.get("/{artist_id}", response_model=output_model)
    @inject
    async def get_artist(
        artist_id: UUID,
        use_cases: FromDishka[QueryArtistUseCases],
    ):
        return await use_cases.execute_read_artist(artist_id)

    @staticmethod
    @api_router.get("/", response_model=list[output_model])
    @inject
    async def get_artists_list(
        use_cases: FromDishka[QueryArtistUseCases],
        filters: ArtistFilter = FilterDepends(ArtistFilter),
    ):
        return await use_cases.execute_read_artists(filters)

    @staticmethod
    @api_router.post("/", response_model=output_model)
    @inject
    async def create_artist(
        command: input_model,
        use_cases: FromDishka[CommandArtistUseCases],
    ):
        return await use_cases.execute_create_artist(**command.model_dump())

    @staticmethod
    @api_router.patch("/{artist_id}", response_model=output_model)
    @inject
    async def update_artist(
        artist_id: UUID,
        command: input_model,
        use_cases: FromDishka[CommandArtistUseCases],
    ):
        return await use_cases.execute_update_artist(
            **command.model_dump(), artist_id=artist_id
        )

    @staticmethod
    @api_router.delete("/{artist_id}", response_model=ResponseStatusModel)
    @inject
    async def delete_artist(
        artist_id: UUID,
        use_cases: FromDishka[CommandArtistUseCases],
    ) -> ResponseStatusModel:
        is_deleted = await use_cases.execute_delete_artist(artist_id=artist_id)
        return ResponseStatusModel(status=is_deleted)
