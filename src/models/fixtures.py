from pydantic import BaseModel, Field
from models.policy import DTOConfig, DTOModuleConfig
from asyncio import Lock


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


class Leds(BaseModel):
    model_config = DTOConfig
    start: int = Field(ge=0)
    stop: int = Field(gt=0)
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
