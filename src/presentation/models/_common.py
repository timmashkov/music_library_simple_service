from datetime import datetime

from pydantic import BaseModel, Field


class ResponseStatusModel(BaseModel):
    status: bool


class ResponseModelWithAliasID(BaseModel):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True


class DateTimeFieldsResponse(BaseModel):
    created_at: datetime | None
    updated_at: datetime | None
