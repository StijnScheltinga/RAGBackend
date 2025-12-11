from fastapi import APIRouter, UploadFile, HTTPException, Depends
from pathlib import Path
from typing import Annotated
from app.db.models import Document, FileStatus
from app.schemas.document import DocumentListResponse
from sqlalchemy.orm import Session
from app.db import get_db
from app.workers.tasks import process_document
import shutil

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")

@router.post("")
def upload(session: Annotated[Session, Depends(get_db)], file: UploadFile):
	if not file.filename:
		raise HTTPException(status_code=400, detail="Empty filename")

	try:
		# Create document record first (this will generate UUID in PostgreSQL)
		document = Document(
			filename=file.filename,
			file_path="",  # Temporary, will update after we get UUID
			file_status=FileStatus.UPLOADED,
			content_type=file.content_type,
			file_size=file.size
		)
		session.add(document)
		session.flush()  # Flush to get the UUID from database without committing
		
		# Now we have the UUID, construct the file path
		file_extension = Path(file.filename).suffix
		uuid_filename = f"{document.id}{file_extension}"
		file_path = UPLOAD_DIR / uuid_filename
		
		# Save the file with UUID-based filename
		with open(file_path, "wb") as buffer:
			shutil.copyfileobj(file.file, buffer)
		
		# Update document with the actual file path
		document.file_path = str(file_path)
		session.commit()

		# Send document to dramatiq for processing
		process_document.send(str(document.id))
		
		return {
			"message": "File uploaded successfully",
			"document_id": str(document.id),
			"original_filename": file.filename,
			"stored_filename": uuid_filename
		}
	except Exception as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@router.get("", response_model=DocumentListResponse)
def list_documents(session: Annotated[Session, Depends(get_db)]):
	documents = session.query(Document).all()
	return DocumentListResponse(
		documents=documents,
		total=len(documents)
	)
