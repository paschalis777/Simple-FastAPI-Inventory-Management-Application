from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    model: str
    price: float

class UpdateItem(BaseModel):
    name: str
    model: str
    price: float

inventory = {
    1: {
        "name": "samsung",
        "model": "s23",
        "price": 850.00,
    },
    2: {
        "name": "apple",
        "model": "15 pro max",
        "price": 1300.00,
    },
    3: {
        "name": "huawei",
        "model": "p 40",
        "price": 550.00,
    },
    4: {
        "name": "nokia",
        "model": "3210",
        "price": 200.00,
    }
}

contact_info = {
    "name": "Paschalis",
    "lastname": "Tsiolas",
    "mail": "paschalis777@outlook.com",
    "github": "paschalis777"
}

about_us = {
    "This is a Python application using the FastAPI "
    "framework to create a simple web service for managing "
    "an inventory of items. It provides endpoints for performing CRUD "
    "(Create, Read, Update, Delete) operations on items in the inventory. "
    "Here's an explanation of what each part of the code does: "
}


# ------------GET------------------------
@app.get("/home")
async def home():
    return {"message": "Hello Welcome To Home Page"}


@app.get("/shop/{item_id}")  #??????????
async def shop(item_id: int):
    return inventory.get(item_id, {"error": "Item not found"})


@app.get("/about")
async def about():
    return about_us


@app.get("/contact")
async def contact():
    return contact_info

# -------------------POST-------------------------
@app.post("/create_item/{item_id}")
async def create_item(item_id: int, item: Item = Body(..., description="Item details")): ????????????
    if item_id in inventory:
        return {"error": "Item already exists"}
    inventory[item_id] = item.dict()
    return {"message": f"Item {item_id} created", "item_details": item}

# --------------------UPDATE----------------------

@app.put("/update_item/{item_id}")
async def update_item(item_id: int, item: UpdateItem = Body(..., description="Item details")):
    if item_id not in inventory:
        return {"error": "Item does not exist"}
    inventory[item_id].update(item.dict())
    return {"message": f"Item {item_id} updated", "item_details": inventory[item_id]}

# -------------------DELETE-------------------------


@app.delete("/delete/{item_id}")
async def delete_item(item_id: int):
    if item_id not in inventory:
        return {"error": "Item not found"}
    del inventory[item_id]
    return {"message": f"Item {item_id} deleted"}









