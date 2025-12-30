from typing import Any

from fastapi_filter.contrib.mongoengine import Filter


class _APIFilter(Filter):

    def custom_filter(self) -> dict[str, Any]:
        filters = self.model_dump()
        filters.pop("sorted_by")
        return {key: value for key, value in filters.items() if value is not None}

    def custom_sort(self) -> list[str]:
        return self.sorted_by
