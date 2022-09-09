from fastapi import APIRouter, Depends
from authx import RedisBackend, User,  Authentication, BaseDBBackend
from authx.core.jwt import JWTBackend

# from synchit_backend.app.application import get_app


# app = get_app()
# auth = app.state.auth

auth = Authentication(
    database_backend=BaseDBBackend(),
    debug = True,
    base_url = 'http://localhost:8000',
    site = 'authx',
    recaptcha_secret = None,
    smtp_username = None,
    smtp_password = None,
    smtp_host = None,
    smtp_tls = False,
    display_name = 'authx',
    private_key=None,
    public_key=None,
    access_expiration=3600,
    refresh_expiration=3600,
    access_cookie_name=None, 
    refresh_cookie_name=None,
    callbacks=None, 
    social_providers=None,
    social_creds=None,
)


auth_router = APIRouter()

# Set up Pre-configured Routes
auth_router.include_router(auth.auth_router, prefix="/api/users") # Login, Register
auth_router.include_router(auth.social_router, prefix="/auth") # Social Login
# auth_router.include_router(auth.password_router, prefix="/api/users")


# Set Redis Cache
auth.set_cache(RedisBackend)
