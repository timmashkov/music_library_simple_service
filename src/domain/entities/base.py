from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

from bson import ObjectId


@dataclass
class BaseDomainModel:
    name: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
