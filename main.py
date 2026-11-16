# Main entry point of the Call Center project.

from services.def_get_all_not_archived_calls import get_all_not_archived_calls
from services.def_get_callinfo_by_id import get_callinfo_by_id
from services.def_archive_call import archive_call


# Display all calls that are not archived.
print("=== NON-ARCHIVED CALLS ===")
all_calls = get_all_not_archived_calls()

for call in all_calls:
    print(call)


# Display a specific call by its ID.
print("\n=== CALL DETAILS ===")
call = get_callinfo_by_id(1001)
print(call)

if call:
    print("Notes:")
    for note in call.notes:
        print(f"- {note.content}")


# Archive a specific call by its ID.
print("\n=== ARCHIVE CALL ===")
archived_call = archive_call(1002)
print(archived_call)