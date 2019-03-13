from document import Document
from mediaType import MediaType


class ContainerDocument(Document):

    MIME_TYPE = "application/vnd.lime.container+json"

    def __init__(self, value=None):
        super().__init__(MediaType.Parse(ContainerDocument.MIME_TYPE))
        self.Value = value

    def GetDocument(self):
        return self.Value

    def GetDocumentJson(self):
        return self.Value.ToJson()

    def SetDocument(self, document):
        self.Value = document

    @staticmethod
    def Type():
        return MediaType.Parse(ContainerDocument.MIME_TYPE)

    def ValueType(self):
        return self.Value.GetMediaType()

    def ToJson(self):
        return {
            'type': str(self.ValueType()),
            'value': self.GetDocumentJson()
        }
