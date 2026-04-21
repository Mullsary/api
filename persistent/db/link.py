from persistent.db.base import Base, WithId, WithCreatedAt,WithUpdatedAt
from sqlalchemy import Column, Text


class Link(Base, WithId, WithCreatedAt,WithUpdatedAt):
    __tablename__ = "link"

    short_link = Column(Text, nullable=False, unique=True)
    long_link = Column(Text, nullable=False)