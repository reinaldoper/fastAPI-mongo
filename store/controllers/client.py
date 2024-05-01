from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4, ValidationError
from store.core.exceptions import NotFoundException

from store.schemas.client import ClientIn, ClientOut, ClientUpdate, ClientUpdateOut
from store.usecases.client import ClientUsecase

router = APIRouter(tags=["clients"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ClientIn = Body(...), usecase: ClientUsecase = Depends()
) -> ClientOut:
    try:
        if (not body.name or len(body.name) == 0) and (body.quantity is None or body.quantity <= 0) and (body.product_id is None or body.product_id != UUID4):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid params")
        else:
            return await usecase.create(body=body)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.message)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e.message))


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ClientUsecase = Depends()
) -> ClientOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ClientUsecase = Depends()) -> List[ClientOut]:
    return await usecase.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ClientUpdate = Body(...),
    usecase: ClientUsecase = Depends(),
) -> ClientUpdateOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ClientUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
