from node import Node
import uuid


class Envelope:

    def __init__(self, id, fromN, to):
        if id is None:
            id = str(uuid.uuid4())
        self.Id = id  # String
        if isinstance(fromN, str):
            fromN = Node.Parse(fromN)
        if isinstance(to, str):
            to = Node.Parse(to)
        self.From = fromN
        self.To = to

    def ToJson(self):
        return {
            'id': self.Id,
            'to': str(self.To),
            'from': str(self.From)
        }
