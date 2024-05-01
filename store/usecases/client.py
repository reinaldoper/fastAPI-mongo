from typing import List
from uuid import UUID
from fastapi.exceptions import ResponseValidationError
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store.db.mongo import db_client
from store.models.client import ClientModel
from store.usecases.product import product_usecase
from store.schemas.client import ClientIn, ClientOut, ClientUpdate, ClientUpdateOut
from store.core.exceptions import NotFoundException


class ClientUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("clients")

    async def create(self, body: ClientIn) -> ClientOut:
        product = await product_usecase.get(body.product_id)
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {body.product_id}")
        client_model = ClientModel(**body.model_dump())
        await self.collection.insert_one(client_model.model_dump())

        return ClientOut(**client_model.model_dump())

    async def get(self, id: UUID) -> ClientOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Client not found with filter: {id}")

        return ClientOut(**result)

    async def query(self) -> List[ClientOut]:
        return [ClientOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ClientUpdate) -> ClientUpdateOut:
        client = await self.collection.find_one({"id": id})
        if not client:
            raise NotFoundException(message=f"Client not found with filter: {id}")
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ClientUpdateOut(**result)
        
    async def delete(self, id: UUID) -> bool:
        client = await self.collection.find_one({"id": id})
        if not client:
            raise NotFoundException(message=f"Client not found with filter: {id}")

        client = await self.collection.delete_one({"id": id})

        return True if client.deleted_count > 0 else False


client_usecase = ClientUsecase()
