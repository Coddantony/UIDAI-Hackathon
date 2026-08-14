from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.auth import auth
from routes.user import user
from routes.verifier import verifier
from routes.health import health
from middleware.security import SecurityHeadersMiddleware, RateLimitMiddleware
from config.indexes import ensure_indexes
import os

app = FastAPI(
    title="uVerifier API",
    description="Privacy-first identity verification API for the UIDAI hackathon.",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if origin.strip()]
if origins == ["*"] and os.getenv("ENVIRONMENT", "development").lower() == "production":
    raise RuntimeError("CORS_ORIGINS must be explicitly configured in production")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=origins != ["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)
app.add_middleware(RateLimitMiddleware, requests_per_minute=int(os.getenv("RATE_LIMIT_PER_MINUTE", "120")))
app.add_middleware(SecurityHeadersMiddleware)


@app.on_event("startup")
async def startup():
    await ensure_indexes()


@app.get("/", response_class=RedirectResponse)
async def home():
    return "/docs"


app.include_router(health, prefix="/api/v1")
app.include_router(auth, prefix="/api/v1/user")
app.include_router(user, prefix="/api/v1/user")
app.include_router(verifier, prefix="/api/v1/verifier")

# Backward-compatible routes for existing clients.
app.include_router(auth, prefix="/user")
app.include_router(user, prefix="/user")
app.include_router(verifier, prefix="/verifier")
