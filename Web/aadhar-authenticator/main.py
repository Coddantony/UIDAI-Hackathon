from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.auth import auth
from routes.user import user
from routes.verifier import verifier
from routes.health import health
from middleware.security import SecurityHeadersMiddleware
import os

app = FastAPI(
    title="uVerifier API",
    description="Aadhar-backed identity verification API for hackathon demos.",
    version="2.0.0",
)

origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "*").split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=origins != ["*"],
    allow_methods=["GET", "POST", "PUT", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)
app.add_middleware(SecurityHeadersMiddleware)


@app.get("/", response_class=RedirectResponse)
async def home():
    return "/docs"


app.include_router(health, prefix="/api/v1")
app.include_router(auth, prefix="/api/v1/user")
app.include_router(user, prefix="/api/v1/user")
app.include_router(verifier, prefix="/api/v1/verifier")
