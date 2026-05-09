from pydantic import ConfigDict

DTO_CONFIG = ConfigDict(frozen=True, use_enum_values=True, extra="forbid", kind="DTO")
DTO_CONFIG_ = ConfigDict(
    frozen=True,
    use_enum_values=True,
    extra="forbid",
    arbitrary_types_allowed=True,
    kind="DTO",
)
