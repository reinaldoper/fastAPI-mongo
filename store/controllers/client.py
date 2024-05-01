from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from fastapi.exceptions import ResponseValidationError
from pydantic import UUID4, ValidationError
from store.core.exceptions import NotFoundException

from store.schemas.client import ClientIn, ClientOut, ClientUpdate, ClientUpdateOut
from store.usecases.client import ClientUsecase

router = APIRouter(tags=["clients"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ClientIn = Body(...), usecase: ClientUsecase = Depends()
) -> ClientOut:
    if not body.name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required")
    if body.quantity is None or body.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid quantity")
    if body.product_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product_id is required")
    
    try:
        return await usecase.create(body=body)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


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
    except ResponseValidationError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"CLient not found with id: %s" % id)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ClientUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
