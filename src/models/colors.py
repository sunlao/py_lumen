from pydantic import BaseModel, Field
from models.policy import DTO_CONFIG


class RGB(BaseModel):
    model_config = DTO_CONFIG
    red: int = Field(ge=0, le=255)
    green: int = Field(ge=0, le=255)
    blue: int = Field(ge=0, le=255)


class Colors(BaseModel):
    model_config = DTO_CONFIG
    name: str
    ordinal: int = Field(ge=0)
    rgb: RGB
