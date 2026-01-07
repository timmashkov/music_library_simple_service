from application.config import settings
from application.server import APIServer
from presentation.routers.album import AlbumRouter
from presentation.routers.artist import ArtistRouter
from presentation.routers.track import TrackRouter

music_app = APIServer(
    name=settings.NAME,
    routers=[ArtistRouter().api_router, AlbumRouter().api_router, TrackRouter().api_router],
    start_callbacks=[],
    stop_callbacks=[],
).app
