from store.models.base_client import CreateClientBaseModel
from store.schemas.client import ClientIn


class ClientModel(ClientIn, CreateClientBaseModel):
    ...
