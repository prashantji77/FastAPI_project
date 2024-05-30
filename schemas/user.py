# def userEntity(item) -> dict:
#     return{
#         "id":str(item["_id"]),
#         "name":str(item["name"]),
#         "email":str(item["email"]),
#         "password":str(item["password"]),

#     }

# def usersEntity(entity) -> list:
#     return[userEntity(item) for item in entity]

from typing import List
from models.user import User

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> List[dict]:
    return [userEntity(item) for item in entity]
