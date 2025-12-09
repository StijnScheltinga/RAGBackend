from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import func
from datetime import datetime


class UUIDMixin:

    @declared_attr
    def id(cls):
        return Column[UUID](
            UUID[UUID](as_uuid=True),
            primary_key=True,
            server_default=func.uuidv7(),  # PostgreSQL 18 native UUID7 function
            nullable=False,
        )


class Document(UUIDMixin, Base):
    __tablename__ = "documents"

    filename = Column[str](String, nullable=False)
    file_path = Column[str](String, nullable=False)
    content_type = Column[str](String, nullable=True)
    file_size = Column[int](Integer, nullable=True)
    created_at = Column[datetime](DateTime, server_default=func.now(), nullable=False)

