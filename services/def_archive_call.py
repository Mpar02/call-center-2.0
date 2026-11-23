# Archives a call based on its ID.

from seed.data import calls


def archive_call(call_id):
    for call in calls:
        if call.id == call_id:
            call.is_archived = True
            return call

    return None