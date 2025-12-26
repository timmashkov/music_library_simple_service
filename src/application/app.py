from application.config import settings
from application.server import APIServer
from presentation.routers.artist import ArtistRouter

music_app = APIServer(
    name=settings.NAME,
    routers=[ArtistRouter().api_router],
    start_callbacks=[],
    stop_callbacks=[],
).app
