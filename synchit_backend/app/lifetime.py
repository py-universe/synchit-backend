from typing import Awaitable, Callable
from fastapi import FastAPI

from synchit_backend.integrations.redis.lifetime import (
    init_redis, shutdown_redis
)
from synchit_backend.db.base import Base
from synchit_backend.db.database import engine


def register_startup_event(app: FastAPI) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    inthe state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        
        # Create database tables. We are going with this approach
        # For simplicity and brevity's sake. In a real-world scenario,
        # We'd be using Alembic to create tables and manage migrations.
        Base.metadata.create_all(bind=engine)

        init_redis(app)
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(app: FastAPI) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        await shutdown_redis(app)
        pass  # noqa: WPS420

    return _shutdown
