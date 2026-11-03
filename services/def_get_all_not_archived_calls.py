#The function that returns all calls that#
#are NOT ARCHIEVED.#


from seed.data import calls


def get_all_not_archived_calls():
    not_archived_calls = []

    for call in calls:
        if call.is_archived == False:
            not_archived_calls.append(call)

    return not_archived_calls