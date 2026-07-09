from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ResearchStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=5, max_length=500, description="Research question or topic")

class ResearchResponse(BaseModel):
    id: str
    status: ResearchStatus
    created_at: datetime

class ResearchResult(BaseModel):
    id: str
    status: ResearchStatus
    topic: str
    report_markdown: Optional[str] = None
    error: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None