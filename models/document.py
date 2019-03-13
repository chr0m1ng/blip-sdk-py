from mediaType import MediaType


class Document:

    def __init__(self, mediaType):

        if mediaType is None:
            raise TypeError

        self._mediaType = mediaType

    def GetMediaType(self):
        if self._mediaType is not None:
            return self._mediaType
        return None

    def ToJson(self):
        return {
            'type': self.GetMediaType()
        }
