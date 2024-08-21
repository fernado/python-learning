from typing import Annotated, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }
@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=False)]):
    results = {"item_id": item_id, "item": item}
    return results