from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from synchit_backend.app.rest_api.router import api_router
from synchit_backend.app.lifetime import register_startup_event, register_shutdown_event
from synchit_backend.logging import configure_logging


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="synchit_backend",
        description="backend for synchit, a group music listening application",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    allow_all = ['*']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_all,
        allow_credentials=True,
        allow_methods=allow_all,
        allow_headers=allow_all
    )
    
    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
