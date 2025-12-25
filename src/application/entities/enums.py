from enum import StrEnum


class ArtistType(StrEnum):
    PERSON = "person"
    BAND = "band"
    ORCHESTRA = "orchestra"
    COMPOSER = "composer"


class Genres(StrEnum):
    METAL = "metal"
    ROCK = "rock"
    POP = "pop"
    RAP = "rap"


class AlbumType(StrEnum):
    LP = "lp"
    EP = "ep"
    DOUBLE = "double"
    TRIPLE = "triple"
    BOX_SET = "box_set"
    MIXTAPE = "mixtape"
