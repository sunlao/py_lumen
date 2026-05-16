from asyncio import Lock
from pydantic import BaseModel, Field
from models.policy import DTOConfig, DTOModuleConfig


class Zone(BaseModel):
    model_config = DTOConfig
    name: str
    ordinal: int = Field(gt=0)
    start: int = Field(ge=0)
    stop: int = Field(gt=0)


class Zones(BaseModel):
    model_config = DTOConfig
    name: str
    description: str
    group: tuple[Zone, ...]

class ColorSet(BaseModel):
    model_config = DTOModuleConfig
    ordinal: int = Field(gt=0)
    leds: tuple[int, ...]

class Frame(BaseModel):
    model_config = DTOModuleConfig
    name: str
    ordinal: int = Field(gt=0)
    color_sets: tuple[ColorSet, ...]

class Gobo(BaseModel):
    model_config = DTOModuleConfig
    name: str
    description: str
    frames: tuple[Frame, ...]

class Leds(BaseModel):
    model_config = DTOConfig
    start: int = Field(ge=0)
    stop: int = Field(gt=0)
    gobos: tuple[Gobo, ...] | None = None
    zones: tuple[Zones, ...] | None = None


class Fixture(BaseModel):
    model_config = DTOModuleConfig
    name: str
    description: str
    leds: Leds
    lock: Lock


class Fixtures(BaseModel):
    model_config = DTOModuleConfig
    name: str
    description: str
    fixtures: tuple[Fixture, ...]
