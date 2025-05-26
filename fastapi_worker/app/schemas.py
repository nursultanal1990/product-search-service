from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class BaseSchema(BaseModel):  # type: ignore

    model_config = ConfigDict(
        from_attributes=True,
    )


class ProductBase(BaseSchema):
    id: str = Field(..., max_length=64)
    name: str
    description: str | None = None
    created_at: datetime
