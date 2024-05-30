from fastapi import APIRouter
from models.user import User
from config.db import client
from schemas.user import userEntity,usersEntity
from bson import ObjectId

user=APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(client.db.users.find())
     

@user.post('/')
async def create_user(user: User):
    new_user = dict(user)
    result = client.db.users.insert_one(new_user)
    return userEntity(client.db.users.find_one({"_id": result.inserted_id}))