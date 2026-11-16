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
        created_at,
        customer=None,
        agent=None,
        notes=None
    ):
        self.id = id
        self.direction = direction
        self.from_number = from_number
        self.to_number = to_number
        self.call_type = call_type
        self.duration = duration
        self.is_archived = is_archived
        self.created_at = created_at
        self.customer = customer
        self.agent = agent
        self.notes = notes if notes is not None else []

    # Returns a readable representation of a call.
    def __repr__(self):
        return (
            f"Call(id={self.id}, "
            f"customer={self.customer}, "
            f"direction={self.direction}, "
            f"call_type={self.call_type}, "
            f"is_archived={self.is_archived})"
        )