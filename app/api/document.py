from fastapi import APIRouter, UploadFile, HTTPException
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")

@router.post("")
def upload(file: UploadFile):
	if not file.filename:
		raise HTTPException(status_code=400, detail="Empty filename")

	try:
		pass
	except Exception as e:
		pass
	
	return {"message": f"{file.filename}"}
