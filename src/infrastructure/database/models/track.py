from application.entities.enums import TrackFormat
from infrastructure.database.models._base import BaseMongoModel


class Track(BaseMongoModel):

    duration: int
    audio_url: str | None
    bitrate: str
    format: TrackFormat
