from fastapi.routing import APIRouter
from synchit_backend.app.rest_api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
