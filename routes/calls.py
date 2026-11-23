from models.api_responses import CallResponse, CallDetailResponse, NoteResponse
from fastapi import APIRouter, HTTPException

from services.def_get_all_not_archived_calls import get_all_not_archived_calls
from services.def_get_callinfo_by_id import get_callinfo_by_id
from services.def_archive_call import archive_call

router = APIRouter()



@router.get("/calls", response_model=dict[str, list[CallResponse]])
def get_calls():
    calls = get_all_not_archived_calls()

    return {
        "calls": [
            CallResponse(
                id=call.id,
                direction=call.direction,
                from_=call.from_number,
                to=call.to_number,
                call_type=call.call_type,
                duration=call.duration,
                is_archived=call.is_archived,
                created_at=call.created_at
            )
            for call in calls
        ]
    }





@router.get("/calls/{call_id}", response_model=CallDetailResponse)
def get_call(call_id: str):
    if not call_id.isdigit():
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    call = get_callinfo_by_id(int(call_id))


    if call is None:
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    return CallDetailResponse(
        id=call.id,
        direction=call.direction,
        from_=call.from_number,
        to=call.to_number,
        call_type=call.call_type,
        duration=call.duration,
        is_archived=call.is_archived,
        created_at=call.created_at,
        notes=[
            NoteResponse(
                id=note.id,
                content=note.content
            )
            for note in call.notes
        ]
    )




@router.patch("/calls/{call_id}/archive", response_model=CallResponse)
def archive_call_endpoint(call_id: str):
    if not call_id.isdigit():
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    call = archive_call(int(call_id))


    if call is None:
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    return CallResponse(
        id=call.id,
        direction=call.direction,
        from_=call.from_number,
        to=call.to_number,
        call_type=call.call_type,
        duration=call.duration,
        is_archived=call.is_archived,
        created_at=call.created_at
    )
