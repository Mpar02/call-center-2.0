# Imput: customer's id#
# Output: customer's info#

from seed.data import calls

def get_callinfo_by_id(call_id):
    for call in calls:
        if call["id"] == call_id:
            return call

    return None
#Test: python -c "from def_get_callinfo_by_id import get_callinfo_by_id; print(get_callinfo_by_id(9999))"
#Test: python -c "from def_get_callinfo_by_id import get_callinfo_by_id; print(get_callinfo_by_id(1001))"
## python -m py_compile def_get_callinfo_by_id.py##