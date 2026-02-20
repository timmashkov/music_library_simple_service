from typing import TYPE_CHECKING, List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base

if TYPE_CHECKING:
    from infrastructure.database.models import Album, Track


class Genre(Base):

    name: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, comment="Genre's title"
    )

    description: Mapped[str | None] = mapped_column(Text, comment="Genre's description")

    albums: Mapped[List["Album"]] = relationship(
        secondary="album_genres",
        back_populates="genres",
        lazy="noload",
    )

    tracks: Mapped[List["Track"]] = relationship(
        secondary="track_genres",
        back_populates="genres",
        lazy="noload",
    )
