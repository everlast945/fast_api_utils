from typing import Annotated

from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from apps.items.domain.item import ItemDomain
from apps.items.services import crud
from core.database import get_session

app = FastAPI()

# region middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# endregion

fake_items_db = [{"item_name": "Foerwero"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/", summary='Список Item')
async def list_item(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)) -> list[ItemDomain]:
    return await crud.items_list(session, limit=limit)
    # return fake_items_db[skip: skip + limit]


@app.post("/items/", summary='Создание Item')
async def create_item(request: ItemDomain, session: AsyncSession = Depends(get_session)) -> int:
    name = request.name
    new_item = crud.items_create(session, item=request)
    for num in range(100000):
        request.name = f'{name}-{num}'
        crud.items_create(session, item=request)
    try:
        await session.commit()
        return new_item.id
    except IntegrityError as ex:
        await session.rollback()
        raise Exception("The item is already stored")


@app.get("/items/{item_id}", summary='Чтение Item')
async def read_item(item_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.items_read(session, item_id)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[ItemDomain, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

