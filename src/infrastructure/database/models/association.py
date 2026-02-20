from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class AlbumGenre(Base):
    __table_args__ = (
        UniqueConstraint("album_uuid", "genre_uuid", name="idx_unique_album_genre"),
        {"extend_existing": True},
    )

    album_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("albums.uuid"), primary_key=True
    )
    genre_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("genres.uuid"), primary_key=True
    )


class TrackGenre(Base):
    __table_args__ = (
        UniqueConstraint("track_uuid", "genre_uuid", name="idx_unique_track_genre"),
        {"extend_existing": True},
    )

    track_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("tracks.uuid"), primary_key=True
    )
    genre_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("genres.uuid"), primary_key=True
    )
