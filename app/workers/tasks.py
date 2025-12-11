from uuid import UUID
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from sqlalchemy import Unicode
from app.db import SessionLocal
from app.db.models import Document, FileStatus
from pathlib import Path

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def process_document(document_id: str):
	session = SessionLocal()
	try:
		# Retrieve document object created by endpoint
		document = session.query(Document).filter_by(id=UUID(document_id)).first()
		if not document:
			print("document not found!")
			return
		elif document and document.file_status != FileStatus.UPLOADED:
			print("Document is not in proper state for processing")
			return

		# Verify the file is present
		path = Path(f"{document.file_path}")
		if not path.is_file():
			print("file can not be found")
			return
		
		# For now only accept text and md
		file_extension = Path(document.filename).suffix.lower()
		if file_extension not in [".txt", ".md"]:
			print(f"Unsupported file type: {file_extension}")
			document.file_status == FileStatus.FAILED
			return

		print(f"File found and ready for processing!: {document.file_path}")
		
		# Start processing file
		document.file_status = FileStatus.PROCESSING
		session.commit()

		try:
			text = path.read_text(encoding="utf-8")
		except UnicodeDecodeError as e:
			print(f"Could not decode file: {e}")
			document.file_status == FileStatus.FAILED
			return
		
		print(text)

	finally:
		session.close()

