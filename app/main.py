from fastapi import FastAPI, HTTPException

from app.models import Item
from app.services import (
    calculate_total_quantity,
    create_item,
    get_all_items,
    get_item_by_id,
    is_low_stock,
)

app = FastAPI(title="SDI 4213 Week 3 Testing Lab")


@app.get("/")
def read_root():
    return {"message": "Welcome to the SDI 4213 automated testing lab"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def read_items():
    items = get_all_items()
    return {
        "count": len(items),
        "total_quantity": calculate_total_quantity(items),
        "items": items,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "item": item,
        "low_stock": is_low_stock(item),
    }


@app.post("/items", status_code=201)
def add_item(item: Item):
    try:
        created_item = create_item(item)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return {"item": created_item}
