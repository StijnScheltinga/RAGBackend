from uuid import UUID
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from app.db import SessionLocal
from app.db.models import Document

redis_broker = RedisBroker(host="redis")
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def process_document(document_id: str):
	session = SessionLocal()
	try:
		document = session.query(Document).filter_by(id=UUID(document_id)).first()
		if document:
			print(f"document found!: {document.file_path}")
	finally:
		session.close()
