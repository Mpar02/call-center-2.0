# Archives a call based on its ID.

from seed.data import calls


def archive_call(call_id):
    for call in calls:
        if call.id == call_id:
            call.is_archived = True
            return call

    return None


#Test for syntax errors:
# python -m py_compile def_archive_call.py
#Tests: python -c "from def_archive_call import archive_call; print(archive_call(9999))"
#result :None
#python -c "from def_archive_call import archive_call; print(archive_call(1001))"
#Result : Call archived 
