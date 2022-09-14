from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from .database import session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Create and get database session.

    :yield: database session.
    """
    session: AsyncSession = session_factory()

    try:  # noqa: WPS501
        yield session
    finally:
        await session.commit()
        await session.close()
