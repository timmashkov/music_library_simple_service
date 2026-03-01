from dataclasses import asdict, dataclass
from typing import Any


@dataclass(kw_only=True)
class BaseDomainModel:
    name: str
    data: dict = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
