from pydantic import ConfigDict

DTOConfig = ConfigDict(frozen=True, use_enum_values=True, extra="forbid", kind="DTO")
DTOModuleConfig = ConfigDict(
    frozen=True,
    use_enum_values=True,
    extra="forbid",
    arbitrary_types_allowed=True,
    kind="DTO",
)
