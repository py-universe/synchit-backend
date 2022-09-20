"""
    Create a database instance here
    TODO: Add two functions to initiate and shutdown connection to db-- if possible
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from synchit_backend.settings import settings


engine = create_engine(
    str(settings.db_url),  
    echo=settings.db_echo)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)