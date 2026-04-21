import uuid

from sqlalchemy import Column, Text,DateTime,Double,MetaData
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()
# Base.metadata = MetaData(schema="public")


def _uuid4_as_str() -> str:
    return str(uuid.uuid4())


class WithId:
    __abstract__ = True

    id = Column(Text, default=_uuid4_as_str, primary_key=True)

class WithCreatedAt:
    __abstract__ = True

    created_at = Column(DateTime(timezone=True),default=datetime.utcnow,nullable=False)



class WithUpdatedAt:
    __abstract__ = True

    updated_at = Column(DateTime(timezone=True),default=datetime.utcnow,nullable=False)