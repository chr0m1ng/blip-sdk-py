from envelope import Envelope
from enum import Enum


class Event(Enum):
    Failed = 'failed'
    Accepted = 'accepted'
    Validated = 'validated'
    Authorized = 'authorized'
    Dispatched = 'dispatched'
    Received = 'received'
    Consumed = 'consumed'


class Notification(Envelope):

    def __init__(self, id=None):
        super().__init__(id)

        self.Event = None  # Event
        self.Reason = None  # Reason

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'event': self.Event,
                'reason': self.Reason.ToJson()
            }
        }
