from typing import Annotated

from fastapi import FastAPI, Body

from apps.items.domain.item import ItemDomain

app = FastAPI()

fake_items_db = [{"item_name": "Foerwero"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/", summary='Список Item')
async def list_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.post("/items/", summary='Создание Item')
async def create_item(request: ItemDomain) -> ItemDomain:
    # item = CreateItemMapper.map_request(request)
    # result = CreateItemService(item=item).run()
    # response = CustomMapper2.map_response(result)
    # return response
    return request


@app.get("/items/{item_id}", summary='Чтение Item')
async def read_item(item_id: int):
    return fake_items_db[item_id]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[ItemDomain, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

