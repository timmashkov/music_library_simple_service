from pydantic import BaseModel


class ResponseStatusModel(BaseModel):
    status: bool
