from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from app.db.models import FileStatus


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    file_path: str
    status: FileStatus
    content_type: str | None
    file_size: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DocumentListResponse(BaseModel):
    documents: list[DocumentResponse]
    total: int
