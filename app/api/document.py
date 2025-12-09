from fastapi import APIRouter, UploadFile, HTTPException, Depends
from pathlib import Path
from typing import Annotated
from app.db.models import Document

from sqlalchemy.orm import Session
from pathlib import Path

from app.db import get_db

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")


@router.post("")
def upload(session: Annotated[Session, Depends(get_db)], file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Empty filename")

    # try:
	# 	file_path = 

    #     document = Document(
	# 		filename=file.filename
	# 		file_path
	# 	)
    #     session.add()
    # except Exception as e:
    #     pass

    return {"message": f"{file.filename}"}
