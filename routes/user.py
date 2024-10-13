from fastapi import APIRouter, Depends
from models.user import User 
from config.db import conn 
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from auth.bearer_handler import JWTBearer

user = APIRouter() 

@user.get('/user/', dependencies=[Depends(JWTBearer())])
async def find_all_users():
    return usersEntity(conn.user.find())

@user.get('/user/{id}')
async def find_one_user(id):
    return userEntity(conn.user.find_one({"_id":ObjectId(id)}))

@user.post('/user/')
async def create_user(user: User):
    conn.user.insert_one(dict(user))
    return usersEntity(conn.user.find())

@user.put('/user/{id}')
async def update_user(id,user: User):
    conn.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(conn.user.find_one({"_id":ObjectId(id)}))

@user.delete('/user/{id}')
async def delete_user(id,user: User):
    return usersEntity(conn.user.find_one_and_delete({"_id":ObjectId(id)}))