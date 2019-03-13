from node import Node
import uuid


class Envelope:

    def __init__(self, id=None, fromN=None, to=None):
        if id is None:
            id = str(uuid.uuid4())
        self.Id = id  # String
        if fromN is not None and isinstance(fromN, str):
            fromN = Node.Parse(fromN)
        if to is not None and isinstance(to, str):
            to = Node.Parse(to)
        self.From = fromN
        self.To = to

    def ToJson(self):
        json = {
            'id': self.Id
        }
        if self.To is not None:
            json['to'] = str(self.To)
        if self.From is not None:
            json['from'] = str(self.From)
        return json
