from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class BaseDomainModel:
    name: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
