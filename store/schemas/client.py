

from typing import Optional
from uuid import UUID
from pydantic import Field

from store.schemas.base_client import BaseClientSchemaMixin, OutClientSchema


class ClientBase(BaseClientSchemaMixin):
    name: str = Field(..., description="Client name")
    product_id: UUID = Field(..., description="Product ID")
    quantity: int = Field(..., description="Quantity")


class ClientIn(ClientBase, BaseClientSchemaMixin):
    ...


class ClientOut(ClientIn, OutClientSchema):
    ...


class ClientUpdate(BaseClientSchemaMixin):
    quantity: Optional[int] = Field(None, description="Client quantity")


class ClientUpdateOut(ClientOut):
    ...
