# Main entry point of the Call Center project.

from services.def_get_all_not_archived_calls import get_all_not_archived_calls

from services.def_get_callinfo_by_id import get_callinfo_by_id

from services.def_archive_call import archive_call


# Display all calls that are not archived.
all_calls = get_all_not_archived_calls()
print(all_calls)

# Display a specific call by its ID.
call = get_callinfo_by_id(1001)
print(call)

# Archive a specific call by its ID.
archived_call = archive_call(1002)
print(archived_call)