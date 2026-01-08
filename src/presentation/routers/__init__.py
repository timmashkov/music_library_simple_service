from fastapi import APIRouter
from pydantic import BaseModel


class BaseRouter:
    api_router: APIRouter
    input_model: BaseModel
    output_model: BaseModel
