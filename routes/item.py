from fastapi import APIRouter
from models.item import Item
from config.db import conn
from schemas.item import itemEntity, itemsEntity
from bson import ObjectId
item = APIRouter()

@item.get('/item/')
async def find_all_items():
    return itemsEntity(conn.item.find())

@item.get('/item/{id}')
async def find_one_item(id):
    return itemEntity(conn.item.find_one({"_id":ObjectId(id)}))

@item.post('/item/')
async def create_item(item: Item):
    conn.item.insert_one(dict(item))
    return itemsEntity(conn.item.find())

@item.put('/item/{id}')
async def update_item(id,item: Item):
    conn.item.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(item)
    })
    return itemEntity(conn.item.find_one({"_id":ObjectId(id)}))

@item.delete('/item/{id}')
async def delete_item(id,item: Item):
    return itemsEntity(conn.item.find_one_and_delete({"_id":ObjectId(id)}))