"""
API routes and endpoints
"""

from fastapi import APIRouter
from app.api import document

api_router = APIRouter()
api_router.include_router(document.router, prefix="/documents", tags=["documents"])

