from typing import Any, Tuple

from sqlalchemy import Table
from sqlalchemy.orm import as_declarative, declared_attr

from synchit_backend.db.meta import meta


@as_declarative(metadata=meta)
class Base:
    """
    Base for all models.

    It has some type definitions to
    enhance autocompletion.
    """

    __tablename__: str
    __table__: Table
    __table_args__: Tuple[Any, ...]

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
