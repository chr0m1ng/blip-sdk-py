from envelope import Envelope
from mediaType import MediaType


class Message(Envelope):

    def __init__(self, id=None, fromN=None, to=None, content=None):
        super().__init__(id, fromN, to)
        self._content = content  # Document

    def Type(self):
        if self._content is not None:
            return self._content.GetMediaType()
        else:
            return None

    def SetDocument(self, document):
        self._content = document

    def GetDocument(self):
        return self._content

    def GetDocumentJson(self):
        return self._content.ToJson()

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'type': str(self.Type()),
                'content': self.GetDocumentJson()
            }
        }
