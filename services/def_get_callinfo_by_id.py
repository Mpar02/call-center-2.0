
# Returns call information based on a specific call ID.

from seed.data import calls


def get_callinfo_by_id(call_id):
    for call in calls:
        if call.id == call_id:
            return call

    return None