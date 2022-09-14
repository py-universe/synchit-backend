from fastapi.routing import APIRouter

from synchit_backend.app.rest_api import monitoring
from synchit_backend.app.rest_api import users

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.auth_router)
