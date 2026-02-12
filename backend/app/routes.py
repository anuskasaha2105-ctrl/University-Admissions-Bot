from fastapi import APIRouter
from app.models.request_model import AdmissionRequest
from app.services.scaledown_service import process_query

router = APIRouter()

@router.post("/admission-query")
def handle_query(request: AdmissionRequest):
    response = process_query(request.query)
    return {"response": response}