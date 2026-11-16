from fastapi import APIRouter, HTTPException

from services.def_get_all_not_archived_calls import get_all_not_archived_calls
from services.def_get_callinfo_by_id import get_callinfo_by_id
from services.def_archive_call import archive_call

router = APIRouter()


@router.get("/calls")
def get_calls():
    calls = get_all_not_archived_calls()
    return {"calls": calls}


@router.get("/calls/{call_id}")
def get_call(call_id: int):
    call = get_callinfo_by_id(call_id)

    if call is None:
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    return call

@router.patch("/calls/{call_id}/archive")
def archive_call_endpoint(call_id: int):
    call = archive_call(call_id)

    if call is None:
        raise HTTPException(
            status_code=404,
            detail="Call not found"
        )

    return call