from mediaType import MediaType
from document import Document


class Header:
    def __init__(self, value=None):
        self.Value = value

    def GetMediaType(self):
        if self.Value is not None:
            return self.Value.GetMediaType()
        return None

    def GetValueJson(self):
        if self.Value is not None:
            return self.Value.ToJson()
        return None

    def ToJson(self):
        return {
            'type': str(self.GetMediaType()),
            'value': self.GetValueJson()
        }


class _ListDocument(Document):
    MIME_TYPE = 'application/vnd.lime.list+json'

    def __init__(self, header=None, items=[]):
        super().__init__(MediaType.Parse(_ListDocument.MIME_TYPE))

        if header is not None and not isinstance(header, Header) \
                and isinstance(header, Document):
            header = Header(header)
        elif header is not None and not isinstance(header, Header):
            raise ValueError('The parameter "header" must be a Header model')

        self.Header = header
        self.Items = items

    @property
    def Total(self):
        if self.Items is not None:
            return len(self.Items)
        return None

    def GetHeaderDocument(self):
        if self.Header is not None:
            return self.Header
        return None

    def SetHeaderDocument(self, document):
        self.Header = Header(document)

    def GetHeaderJson(self):
        if self.Header is not None:
            return self.Header.ToJson()
        return None

    def GetItems(self):
        if self.Items is not None:
            return self.Items
        return None

    def GetItemsJson(self):
        if self.Items is not None:
            return [
                {
                    'type': str(x.GetMediaType()),
                    'value': x.ToJson()
                }
                for x in self.Items
            ]
        return None

    def ToJson(self):
        return {
            'header': self.GetHeaderJson(),
            'items': self.GetItemsJson()
        }


class ListDocument(_ListDocument):

    Type = MediaType.Parse(_ListDocument.MIME_TYPE)
