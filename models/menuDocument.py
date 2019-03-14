from mediaType import MediaType
from document import Document
from enum import Enum


class Scope(Enum):
    Transient = 'transient'
    Persistent = 'persistent'
    Immediate = 'imemediate'


class _MenuDocument(Document):

    MIME_TYPE = 'application/vnd.lime.select+json'

    def __init__(self, scope=Scope.Transient, header=None, options=[]):
        super().__init__(MediaType.Parse(_MenuDocument.MIME_TYPE))
        for o in options:
            if not isinstance(o, _MenuDocument.Option):
                raise ValueError(
                    'The parameter "options" must be a list of Option model')
        if not isinstance(scope, Scope):
            raise ValueError('The parameter "scope" must be a Scope model')
        if header is not None and not (isinstance(header, Document) or
                                       isinstance(header, str)):
            raise ValueError(
                'The parameter "header" must be a Document or a string')

        self.Scope = scope
        self.Header = header
        self.Options = options

    @property
    def Total(self):
        return len(self.Options)

    def GetOptionsJson(self):
        return [x.ToJson() for x in self.Options]

    def GetHeaderType(self):
        if self.Header is not None:
            return self.Header.GetMediaType()
        return None

    def GetHeaderJson(self):
        if self.Header is not None:
            return self.Header.ToJson()
        return None

    def ToJson(self):
        json = {
            'scope': self.Scope.value
        }

        if isinstance(self.Header, str):
            json.update({'text': self.Header})
        else:
            json.update({
                'header': {
                    'type': str(self.GetHeaderType()),
                    'value': self.GetHeaderJson()
                }
            })
        json.update({'options': self.GetOptionsJson()})

        return json

    class Option:
        def __init__(self, order=None, label=None, value=None, text=None):
            if order is not None and not isinstance(order, int):
                raise ValueError('The parameter "order" must be a integer')
            if label is not None and not isinstance(label, Document):
                raise ValueError(
                    'The parameter "label" must be a Document model')
            if value is not None and not (isinstance(value, dict) or
                                          isinstance(value, Document)):
                raise ValueError(
                    'The parameter "value" must be a Document model or a Dict')
            if text is not None and not isinstance(text, str):
                raise ValueError('The parameter "text" must be a string')

            self.Order = order
            self.Label = label
            self.Value = value
            self.Text = text

        def GetLabelDocumentJson(self):
            if self.Label is not None:
                return self.Label.ToJson()
            return None

        def GetLabelMediaType(self):
            if self.Label is not None:
                return self.Label.GetMediaType()
            return None

        def GetValueMediaType(self):
            if self.Value is not None:
                if isinstance(self.Value, dict):
                    return MediaType.ApplicationJson
                return self.Value.GetMediaType()
            return None

        def GetValueDocumentJson(self):
            if self.Value is not None:
                if isinstance(self.Value, dict):
                    return self.Value
                return self.Value.ToJson()
            return None

        def ToJson(self):
            json = {}
            if isinstance(self.Order, int):
                json.update({'order': self.Order})
            if self.Text is not None:
                json.update({'text': self.Text})
            elif self.Label is not None:
                json.update({
                    'label': {
                        'type': str(self.GetLabelMediaType()),
                        'value': self.GetLabelDocumentJson()
                    }
                })
            if isinstance(self.Value, Document):
                json.update({
                    'value': {
                        'type': str(self.GetValueMediaType()),
                        'value': self.GetValueDocumentJson()
                    }
                })
            elif isinstance(self.Value, dict):
                json.update({
                    'type': str(self.GetValueMediaType()),
                    'value': self.GetValueDocumentJson()
                })

            return json


class MenuDocument(_MenuDocument):

    Type = MediaType.Parse(_MenuDocument.MIME_TYPE)
