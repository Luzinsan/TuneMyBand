from djantic import ModelSchema
from pydantic import BaseModel

from .models import User

__all__ = ["JWTPairSchema", "CreateUserSchema"]


class JWTPairSchema(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str = "bearer"


class CreateUserSchema(ModelSchema):
    class Config:
        model = User
        include = (
            "username",
            "password",
            "first_name",
            "last_name",
        )
