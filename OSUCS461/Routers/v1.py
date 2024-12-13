from fastapi import APIRouter, HTTPException
from OSUCS461.Classes.Database import UserDB
from OSUCS461.Classes.Database import UserPostDB
from OSUCS461.Models import UserWrite
from OSUCS461.Models import UserPostWrite
from OSUCS461.Utilities.CustomLogger import custom_logger

router = APIRouter()
logger = custom_logger('fastAPI', 'fastapi_logs.log')

#Users
@router.get("/users")
async def get_all_users():
    try:
        return UserDB.get_all()
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.get("/users/{user_id}")
async def get_user(user_id: str):
    try:
        return UserDB.get(user_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.post("/users")
async def create_user(user: UserWrite):
    try:
        uuid = UserDB.create(user)
        return UserDB.get(uuid)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.put("/users/{user_id}")
async def update_user(user_id: str, user: UserWrite):
    try:
        UserDB.update(user_id, user)
        return UserDB.get(user_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        success = UserDB.delete(user_id)
        return {"success": success}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
#UserPost stuff

@router.get("users/{user_id}/posts")
async def get_all_user_post(user_id: str):
    try:
        return UserPostDB.get_all(user_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.get("users/{user_id}/posts/{post_id}")
async def get_user_post(user_id: str, post_id: str):
    try:
        return UserPostDB.get(user_id, post_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
@router.post("users/{user_id}/posts")
async def create_user_post(user_id: str, post: UserPostWrite):
    try:
        uuid = UserPostDB.create(user_id, post)
        return UserPostDB.get(user_id, uuid)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500)
    
