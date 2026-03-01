from .album import ResponseAlbumModel
from .artist import ResponseArtistModel
from .track import ResponseTrackModel

ResponseArtistModel.model_rebuild()
ResponseAlbumModel.model_rebuild()
ResponseTrackModel.model_rebuild()
