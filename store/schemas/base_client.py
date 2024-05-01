from datetime import datetime
from pydantic import UUID4, BaseModel, Field


class BaseClientSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutClientSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

