from pydantic import ConfigDict

DTOConfig = ConfigDict(frozen=True, use_enum_values=True, extra="forbid", kind="DTO")
