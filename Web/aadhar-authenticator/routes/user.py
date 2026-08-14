from fastapi import APIRouter, Depends, HTTPException
from models.user import User, UpdateUser
from config.database import db
from utils.password import get_password_hash
from utils.token import get_current_user, get_current_username
from utils.xmlparser import parse_xml
from typing import List
from models.verifier import VerifierInfo

user = APIRouter()


@user.get('/me',
          response_model=User,
          response_model_exclude={"password"},
          tags=["user"])
async def current_user(current_user: User = Depends(get_current_user)):
    return current_user


@user.put('/me', tags=["user"])
async def update_user(
        user: UpdateUser,
        username: str = Depends(get_current_username)):
    userData = user.dict(exclude_unset=True)
    if userData.get('password'):
        userData['vid'] = userData['password']
        userData['password'] = get_password_hash(userData['password'])
    if userData.get('eKYCXML'):
        userData.update(parse_xml(userData.get("eKYCXML")))
    if not userData:
        raise HTTPException(status_code=400, detail="No fields provided")
    await db.users.update_one(
        {"username": username},
        {"$set": userData})
    return {"success": True}


@user.get('/access_logs',
          response_model=List[VerifierInfo],
          response_model_exclude={"api_key", "vid"},
          tags=["user"])
async def get_access_logs(
        skip: int = 0,
        limit: int = 50,
        username: str = Depends(get_current_username)):
    limit = min(max(limit, 1), 100)
    skip = max(skip, 0)
    user_record = await db.users.find_one({"username": username})
    return await db.access_logs.find(
        {"vid": user_record.get("vid")}
    ).sort("accessedAt", -1).skip(skip).limit(limit).to_list(length=limit)


@user.get('/access_logs/summary', tags=["user"])
async def access_log_summary(username: str = Depends(get_current_username)):
    user_record = await db.users.find_one({"username": username})
    total = await db.access_logs.count_documents({"vid": user_record.get("vid")})
    latest = await db.access_logs.find_one(
        {"vid": user_record.get("vid")}, sort=[("accessedAt", -1)])
    return {
        "total_accesses": total,
        "last_accessed_at": latest.get("accessedAt") if latest else None,
    }
