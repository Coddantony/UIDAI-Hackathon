from dotenv import load_dotenv
import os

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
SECRET_KEY = os.getenv("SECRET_KEY")

if not MONGO_HOST:
    raise RuntimeError("MONGO_HOST is required")
if not MONGO_DBNAME:
    raise RuntimeError("MONGO_DBNAME is required")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is required")
if len(SECRET_KEY) < 32:
    raise RuntimeError("SECRET_KEY must contain at least 32 characters")

MONGO_CONFIG = {"HOST": MONGO_HOST, "DBNAME": MONGO_DBNAME}

JWT_CONFIG = {
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES": 60,
    "REFRESH_TOKEN_EXPIRE_MINUTES": 360,
    "GUEST_TOKEN_EXPIRE_MINUTES": 360,
}

SAMPLE_XML = '<OfflinePaperlessKyc referenceId="00000"></OfflinePaperlessKyc>'
