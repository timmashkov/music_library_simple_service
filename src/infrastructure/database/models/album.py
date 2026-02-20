import typing
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base

if typing.TYPE_CHECKING:
    from infrastructure.database.models import Artist, Track


class Album(Base):

    name: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Album's title"
    )
    description: Mapped[str | None] = mapped_column(Text, comment="Album's description")
    cover_url: Mapped[str | None] = mapped_column(
        String, comment="Cover's url in minio"
    )
    artist_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("artists.uuid"),
        nullable=False,
        index=True,
        comment="Artist's unique id",
    )

    artist: Mapped["Artist"] = relationship(
        "Artist",
        back_populates="albums",
        lazy="noload",
    )

    tracks: Mapped[typing.List["Track"]] = relationship(
        "Track",
        back_populates="album",
        cascade="all, delete-orphan",
        passive_updates=True,
        passive_deletes=True,
        lazy="noload",
    )
