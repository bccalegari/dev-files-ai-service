import uuid


class TraceId:
    def __init__(self, value: str):
        if value is None:
            self.value = str(uuid.uuid4())
        else:
            self.value = value

    def __str__(self):
        return self.value