from envelope import Envelope
from envelopeId import EnvelopeId
from message import Message
from enum import Enum


class CommandMethod(Enum):

    Get = 'get'
    Set = 'set'
    Delete = 'delete'
    Subscribe = 'subscribe'
    Unsubscribe = 'unsubscribe'
    Observe = 'observe'
    Merge = 'merge'


class CommandStatus(Enum):
    Pending = 'pending'
    Success = 'success'
    Failure = 'failure'


class Command(Envelope):

    def __init__(self, id=None, uri=None, resource=None, method=None,
                 status=None, reaspon=None):
        super().__init__(id)

        self.Uri = None  # LimeUri
        self.Resource = None  # Document
        self.Method = None  # CommandMethod
        self.Status = None  # CommandStatus
        self.Reason = None  # Reason

    @property
    def Type(self):
        return self.Resource.GetMediaType()

    def SetDocument(self, document):
        self.Resource = document

    def GetDocument(self):
        if self.Resource is not None:
            return self.Resource
        return None

    def GetDocumentJson(self):
        if self.Resource is not None:
            return self.Resource.ToJson()
        return None

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'method': self.Method,
                'uri': self.Uri,
                'type': self.Type,
                'resource': self.GetDocumentJson()
            }
        }
