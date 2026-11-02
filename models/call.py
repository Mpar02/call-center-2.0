# Defines the structure of a phone call.

class Call:
    def __init__(
        self,
        id,
        direction,
        from_number,
        to_number,
        call_type,
        duration,
        is_archived,
        created_at
    ):
        self.id = id
        self.direction = direction
        self.from_number = from_number
        self.to_number = to_number
        self.call_type = call_type
        self.duration = duration
        self.is_archived = is_archived
        self.created_at = created_at