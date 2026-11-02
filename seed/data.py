#Call records
calls = [
    {
        "id": 1001,
        "customer": "Maria Paraskevopoulou",
        "direction": "inbound",
        "from": "+30 210 1111111",
        "to": "+30 210 2222222",
        "agent": "Sofia Papadopoulou",
        "call_type": "answered",
        "duration": 120,
        "is_archived": False,
        "created_at": "2026-10-28T14:32:00Z",
        
        "notes": [
                    {
                      "id": "note-1",
                      "call_id": 1001,
                      "content": "Customer would like further information about food supplements"
                     }
         ]
     },


     {
        "id": 1002,
        "customer": "Nikos Andreou",
        "direction": "outbound",
        "from": "+30 210 3333333",
        "to": "+30 210 4444444",
        "agent": "Dimitris Georgiou",
        "call_type": "answered",
        "duration": 245,
        "is_archived": False,
        "created_at": "2026-10-27T09:15:00Z",
        "notes": [
                    {
                        "id": "note-2",
                        "call_id": 1002,
                        "content": "Customer requested an update on a previous inquiry"
                    }
                 ]
    },



    {
        "id": 1003,
        "customer": "Eleni Nikolaou",
        "direction": "inbound",
        "from": "+30 210 5555555",
        "to": "+30 210 2222222",
        "agent": "Anna Dimitriou",
        "call_type": "missed",
        "duration": 0,
        "is_archived": False,
        "created_at": "2026-10-26T11:42:00Z",
        "notes": [
                    {
                        "id": "note-3",
                        "call_id": 1003,
                        "content": "Customer called about an issue with a recent order"
                    }
                 ]
    },


    
    {
        "id": 1004,
        "customer": "Giorgos Papas",
        "direction": "outbound",
        "from": "+30 210 3333333",
        "to": "+30 210 6666666",
        "agent": "Sofia Papadopoulou",
        "call_type": "answered",
        "duration": 310,
        "is_archived": False,
        "created_at": "2026-10-25T15:20:00Z",
        "notes": [
                    {
                        "id": "note-4",
                        "call_id": 1004,
                        "content": "Customer showed interest in a new product"
                    }
                 ]
    },



    {
        "id": 1005,
        "customer": "Katerina Ioannou",
        "direction": "inbound",
        "from": "+30 210 7777777",
        "to": "+30 210 2222222",
        "agent": "Maria Antoniou",
        "call_type": "voicemail",
        "duration": 185,
        "is_archived": True,
        "created_at": "2026-10-24T10:05:00Z",
        "notes": [
                    {
                        "id": "note-5",
                        "call_id": 1005,
                        "content": "Customer reported a delayed delivery"
                    }
                 ]
    },



    {
        "id": 1006,
        "customer": "Alexandros Vasileiou",
        "direction": "outbound",
        "from": "+30 210 3333333",
        "to": "+30 210 8888888",
        "agent": "Dimitris Georgiou",
        "call_type": "voicemail",
        "duration": 0,
        "is_archived": False,
        "created_at": "2026-10-23T13:30:00Z",
        "notes": [
                    {
                        "id": "note-6",
                        "call_id": 1006,
                        "content": "No answer; another call attempt may be needed"
                    }
                 ]
    },



    {
        "id": 1007,
        "customer": "Sofia Christou",
        "direction": "inbound",
        "from": "+30 210 9999999",
        "to": "+30 210 2222222",
        "agent": "Anna Dimitriou",
        "call_type": "answered",
        "duration": 95,
        "is_archived": False,
        "created_at": "2026-10-22T16:10:00Z",
        "notes": [
                    {
                        "id": "note-7",
                        "call_id": 1007,
                        "content": "Customer asked about available subscription plans"
                    }
                 ]
    },



    {
        "id": 1008,
        "customer": "Petros Markou",
        "direction": "outbound",
        "from": "+30 210 3333333",
        "to": "+30 210 1212121",
        "agent": "Maria Antoniou",
        "call_type": "answered",
        "duration": 420,
        "is_archived": False,
        "created_at": "2026-10-21T12:45:00Z",
        "notes": [
                    {
                        "id": "note-8",
                        "call_id": 1008,
                        "content": "Agent guided the customer through the account setup"
                    }
                 ]
    },



    {
        "id": 1009,
        "customer": "Dimitra Kostas",
        "direction": "inbound",
        "from": "+30 210 3434343",
        "to": "+30 210 2222222",
        "agent": "Sofia Papadopoulou",
        "call_type": "answered",
        "duration": 160,
        "is_archived": False,
        "created_at": "2026-10-20T08:55:00Z",
        "notes": [
                    {
                        "id": "note-9",
                        "call_id": 1009,
                        "content": "Customer requested clarification about an invoice"
                    }
                 ]
    },



    {
        "id": 1010,
        "customer": "Christos Theodorou",
        "direction": "outbound",
        "from": "+30 210 3333333",
        "to": "+30 210 5656565",
        "agent": "Dimitris Georgiou",
        "call_type": "answered",
        "duration": 275,
        "is_archived": False,
        "created_at": "2026-10-19T14:00:00Z",
        "notes": [
                    {
                        "id": "note-10",
                        "call_id": 1010,
                        "content": "Customer shared positive feedback about the service"
                    }
                 ]
    }

    
]


# Test : python -m py_compile data.py
#Test for the amount of total calls and notes
# python -c "from data import calls; print('Total calls:', len(calls)); print('Total notes:', sum(len(call['notes']) for call in calls))"