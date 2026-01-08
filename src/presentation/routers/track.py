from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases.command_use_caces import CommandTrackUseCases
from application.use_cases.queries_use_caces import QueryTrackUseCases
from presentation.models._common import ResponseStatusModel
from presentation.models.track import CommandTrackModel, ResponseTrackModel, TrackFilter
from presentation.routers import BaseRouter


class TrackRouter(BaseRouter):
    api_router = APIRouter(prefix="/tracks", tags=["tracks"])
    input_model = CommandTrackModel
    output_model = ResponseTrackModel

    @staticmethod
    @api_router.get("/{name}", response_model=output_model)
    @inject
    async def get_track(
        name: str,
        use_cases: FromDishka[QueryTrackUseCases],
    ):
        return await use_cases.execute_read_track(name)

    @staticmethod
    @api_router.get("/", response_model=list[output_model])
    @inject
    async def get_tracks_list(
        use_cases: FromDishka[QueryTrackUseCases],
        filters: TrackFilter = FilterDepends(TrackFilter),
    ):
        return await use_cases.execute_read_tracks(filters)

    @staticmethod
    @api_router.post("/", response_model=output_model)
    @inject
    async def create_track(
        command: CommandTrackModel,
        use_cases: FromDishka[CommandTrackUseCases],
    ):
        return await use_cases.execute_create_track(**command.model_dump())

    @staticmethod
    @api_router.patch("/{artist_id}", response_model=output_model)
    @inject
    async def update_track(
        artist_id: str,
        command: CommandTrackModel,
        use_cases: FromDishka[CommandTrackUseCases],
    ):
        return await use_cases.execute_update_track(
            **command.model_dump(), artist_id=artist_id
        )

    @staticmethod
    @api_router.delete("/{artist_id}", response_model=ResponseStatusModel)
    @inject
    async def delete_track(
        artist_id: str,
        use_cases: FromDishka[CommandTrackUseCases],
    ) -> ResponseStatusModel:
        is_deleted = await use_cases.execute_delete_track(artist_id=artist_id)
        return ResponseStatusModel(status=is_deleted)
