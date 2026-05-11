from pydantic import BaseModel, Field
from models.policy import DTOConfig, DTOModuleConfig
from asyncio import Lock


class Leds(BaseModel):
    model_config = DTOConfig
    start: int
    stop: int


class Fixture(BaseModel):
    model_config = DTOModuleConfig
    name: str
    leds: Leds
    lock: Lock
