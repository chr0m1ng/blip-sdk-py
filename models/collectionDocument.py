from document import Document
from mediaType import MediaType


class CollectionDocument(Document):

    MIME_TYPE = "application/vnd.lime.collection+json"

    def __init__(self, itemType, items=[]):
        super().__init__(MediaType.Parse(CollectionDocument.MIME_TYPE))

        self.Total = 0
        self.ItemType = itemType
        self.Items = items

    @staticmethod
    def Type():
        return MediaType.Parse(CollectionDocument.MIME_TYPE)

    def GetDocuments(self):
        return self.Items

    def GetDocumentsJson(self):
        return [x.ToJson() for x in self.Items]

    def ToJson(self):
        return {
            'itemType': str(self.ItemType),
            'items': self.GetDocumentsJson()
        }
