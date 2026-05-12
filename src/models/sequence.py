from asyncio import sleep
from pydantic import BaseModel, Field
from models.policy import DTOConfig, DTOModuleConfig


class Sequence(BaseModel):
    model_config = DTOModuleConfig
    ordinal: int = Field(gt=0)
    function: 
    params: ()
