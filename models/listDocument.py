from mediaType import MediaType
from document import Document


class Header:
    def __init__(self, value=None):
        self.Value = value

    def GetMediaType(self):
        return self.Value.GetMediaType()

    def GetValueJson(self):
        return self.Value.ToJson()

    def ToJson(self):
        return {
            'type': str(self.GetMediaType()),
            'value': self.GetValueJson()
        }


class ListDocument(Document):
    MIME_TYPE = 'application/vnd.lime.list+json'

    def __init__(self, header=None, items=[]):
        super().__init__(MediaType.Parse(ListDocument.MIME_TYPE))

        if header is not None and not isinstance(header, Header) \
                and isinstance(header, Document):
            header = Header(header)
        elif header is not None and not isinstance(header, Header):
            raise ValueError('The parameter "header" must be a Header model')

        self.Header = header
        self.Items = items

    def Total(self):
        return len(self.Items)

    def GetHeaderDocument(self):
        return self.Header

    def SetHeaderDocument(self, document):
        self.Header = Header(document)

    def GetHeaderJson(self):
        return self.Header.ToJson()

    def GetItems(self):
        return self.Items

    def GetItemsJson(self):
        return [
            {
                'type': str(x.GetMediaType()),
                'value': x.ToJson()
            }
            for x in self.Items
        ]

    @staticmethod
    def Type():
        return MediaType.Parse(ListDocument.MIME_TYPE)

    def ToJson(self):
        return {
            'header': self.GetHeaderJson(),
            'items': self.GetItemsJson()
        }
