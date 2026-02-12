from pydantic import BaseModel

class AdmissionRequest(BaseModel):
    query: str