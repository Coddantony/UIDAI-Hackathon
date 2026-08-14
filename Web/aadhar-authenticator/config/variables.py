from dotenv import load_dotenv
import os

load_dotenv()

MONGO_CONFIG = {
    "HOST": os.getenv("MONGO_HOST"),
    "DBNAME": os.getenv("MONGO_DBNAME"),
}

JWT_CONFIG = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "ALGORITHM": os.getenv("JWT_ALGORITHM", "HS256"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")),
    "REFRESH_TOKEN_EXPIRE_MINUTES": int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", "360")),
    "GUEST_TOKEN_EXPIRE_MINUTES": int(os.getenv("GUEST_TOKEN_EXPIRE_MINUTES", "60")),
}

if not JWT_CONFIG["SECRET_KEY"] and os.getenv("ENVIRONMENT", "development").lower() == "production":
    raise RuntimeError("SECRET_KEY must be configured in production")

SAMPLE_XML = '<OfflinePaperlessKyc referenceId="00000"></OfflinePaperlessKyc>'
