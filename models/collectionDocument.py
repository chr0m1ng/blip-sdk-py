from document import Document
from mediaType import MediaType


class _CollectionDocument(Document):

    MIME_TYPE = "application/vnd.lime.collection+json"

    def __init__(self, itemType, items=[]):
        super().__init__(MediaType.Parse(_CollectionDocument.MIME_TYPE))

        self.ItemType = itemType
        self.Items = items

    @property
    def Total(self):
        return len(self.Items)

    def GetDocuments(self):
        return self.Items

    def GetDocumentsJson(self):
        return [x.ToJson() for x in self.Items]

    def ToJson(self):
        return {
            'itemType': str(self.ItemType),
            'items': self.GetDocumentsJson()
        }


class CollectionDocument(_CollectionDocument):

    Type = MediaType.Parse(_CollectionDocument.MIME_TYPE)
