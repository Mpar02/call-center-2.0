# Returns all calls that are not archived.

from seed.data import calls


def get_all_not_archived_calls():
    not_archived_calls = []

    for call in calls:
        if not call.is_archived:
            not_archived_calls.append(call)

    return not_archived_calls