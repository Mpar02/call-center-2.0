
from pydantic import BaseModel, Field


class NoteResponse(BaseModel):
    id: str
    content: str


class CallResponse(BaseModel):
    id: int
    direction: str
    from_: str = Field(serialization_alias="from")
    to: str
    call_type: str
    duration: int
    is_archived: bool
    created_at: str


class CallDetailResponse(CallResponse):
    notes: list[NoteResponse]
