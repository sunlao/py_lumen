from pydantic import BaseModel, Field
from models.policy import DTOConfig


class RGB(BaseModel):
    model_config = DTOConfig
    red: int = Field(ge=0, le=255)
    green: int = Field(ge=0, le=255)
    blue: int = Field(ge=0, le=255)


class Colors(BaseModel):
    model_config = DTOConfig
    name: str
    ordinal: int = Field(ge=0)
    rgb: RGB


class ColorGroup(BaseModel):
    model_config = DTOConfig
    collection: tuple[Colors, ...]


class ColorMap(BaseModel):
    model_config = DTOConfig
    ordinal: int = Field(ge=0)
    rgb: RGB

class FrameColorSet(BaseModel):
    model_config = DTOConfig
    name: str
    color_maps: tuple[ColorMap, ...]

class FrameColorSets(BaseModel):
    model_config = DTOConfig
    frame_color_sets: tuple[FrameColorSet, ...]