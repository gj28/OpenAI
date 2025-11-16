from pydantic import BaseModel
from typing import Any, Dict, List


class Component(BaseModel):
    id: str
    name: str
    status: str


class IncidentUpdate(BaseModel):
    id: str
    status: str
    body: str
    created_at: str


class Incident(BaseModel):
    id: str
    name: str
    status: str
    incident_updates: List[IncidentUpdate] = []


class WebhookPayload(BaseModel):
    data: Dict[str, Any]
