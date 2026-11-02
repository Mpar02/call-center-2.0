# Defines the structure of a note.

class Note:
    def __init__(self, id, call_id, content):
        self.id = id
        self.call_id = call_id
        self.content = content