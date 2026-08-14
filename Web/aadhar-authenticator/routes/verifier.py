from fastapi import APIRouter, HTTPException, Query
from models.verifier import Verifier, LoginVerifier, VerifierInfo
from models.user import User
from config.database import db
from utils.password import get_password_hash, verify_password
from utils.identity import fingerprint
from datetime import datetime
from pymongo import ReturnDocument
import uuid

verifier = APIRouter()


@verifier.post('/register', tags=["verifier"])
async def create_verifier(admin: Verifier):
    admin.password = get_password_hash(admin.password)
    admin.isActive = True
    admin.createdAt = datetime.utcnow()
    admin.lastLogin = None
    record = await db.verifiers.find_one({"username": admin.username})
    if record is not None:
        return {"success": False, "error": "UserName Already Exists"}
    admin.api_key = str(uuid.uuid4())
    admin = dict(admin)
    await db.verifiers.insert_one(admin)
    admin.pop("password", None)
    return admin


@verifier.post('/login', response_model=Verifier, response_model_exclude={"password"}, tags=["verifier"])
async def login_verifier(login: LoginVerifier):
    user = await db.verifiers.find_one({"username": login.username})
    if not user or not user.get("isActive", True) or not verify_password(login.password, user.get("password")):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return await db.verifiers.find_one_and_update(
        {"_id": user["_id"]},
        {"$set": {"lastLogin": datetime.utcnow()}},
        return_document=ReturnDocument.AFTER,
    )


@verifier.get('/api/{api_key}', response_model=User, response_model_include={"eKYCXML", "name", "dob", "gender"}, tags=["verifier"])
async def fetch_user(api_key: str, vid: str = Query(min_length=1, max_length=255)):
    verifier_record = await db.verifiers.find_one({"api_key": api_key, "isActive": True})
    if not verifier_record:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user = await db.users.find_one({"vid_fingerprint": fingerprint(vid), "isActive": True})
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    vlog = VerifierInfo(
        vid="redacted",
        api_key=api_key,
        name=verifier_record.get("name"),
        accessedAt=datetime.utcnow(),
    )
    await db.access_logs.insert_one(dict(vlog))
    return user
