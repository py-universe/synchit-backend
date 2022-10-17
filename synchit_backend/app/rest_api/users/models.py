from sqlalchemy import Boolean, Column, String

from synchit_backend.db.base import Base


# The goal with this is to extend the firebase user
class UserProfile(Base):
    id = Column(String, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    # Maybe link a user the their current room here