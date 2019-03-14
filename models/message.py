from envelope import Envelope
from mediaType import MediaType


class Message(Envelope):

    def __init__(self, id=None, fromN=None, to=None, content=None):
        super().__init__(id, fromN, to)
        self._content = content  # Document

    @property
    def Type(self):
        if self._content is not None:
            if isinstance(self._content, dict):
                return MediaType.ApplicationJson
            return self._content.GetMediaType()
        else:
            return None

    def SetDocument(self, document):
        self._content = document

    def GetDocument(self):
        if self._content is not None:
            return self._content
        return None

    def GetDocumentJson(self):
        if self._content is not None:
            if isinstance(self._content, dict):
                return self._content
            return self._content.ToJson()
        return None

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'type': str(self.Type),
                'content': self.GetDocumentJson()
            }
        }
