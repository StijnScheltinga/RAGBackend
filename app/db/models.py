import enum
from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import func
from datetime import datetime


class FileStatus(enum.Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"


class UUIDMixin:

    @declared_attr
    def id(cls):
        return Column[UUID](
            UUID[UUID](as_uuid=True),
            primary_key=True,
            server_default=func.uuidv7(),  # PostgreSQL 18 native UUID7 function
            nullable=False,
        )


class TimestampMixin:

    @declared_attr
    def created_at(cls):
        return Column[datetime](DateTime, server_default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column[datetime](
            DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
        )


class Document(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "documents"

    filename = Column[str](String, nullable=False)
    file_path = Column[str](String, nullable=False)
    file_status = Column[enum.Enum](Enum(FileStatus, name='file_status'), nullable=False)
    content_type = Column[str](String, nullable=True)
    file_size = Column[int](Integer, nullable=True)

class Chunk(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "chunks"

    document_id = Column[UUID](UUID[UUID](), ForeignKey('documents.id', ondelete='CASCADE'), nullable=False, index=True)
    position = Column[int](Integer, nullable=False)
    text = Column[str](String, nullable=False)