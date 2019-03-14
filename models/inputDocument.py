from plainTextDocument import PlainTextDocument
from mediaType import MediaType
from document import Document
from enum import Enum


class Rule(Enum):
    Type = 'type'
    Text = 'text'


class Validation:
    def __init__(self, rule, mediaType=None):
        if not isinstance(rule, Rule):
            raise ValueError('The parameter "rule" must be a Rule Model')
        if rule == Rule.Type:
            if mediaType is None:
                raise TypeError
        self.MediaType = mediaType
        self.Rule = rule

    def ToJson(self):
        json = {
            'rule': self.Rule.value
        }
        if self.MediaType is not None:
            json.update({'type': str(self.MediaType)})

        return json


class _InputDocument(Document):

    MIME_TYPE = 'application/vnd.lime.input+json'

    def __init__(self, label=None, validation=None):
        super().__init__(MediaType.Parse(_InputDocument.MIME_TYPE))

        if isinstance(label, str):
            label = PlainTextDocument(label)
        self.Label = label  # PlainText
        if isinstance(validation, Validation):
            self.Validation = validation
        elif validation is not None:
            raise ValueError(
                'The parameter "validation" must be a Validation Model')

    def GetLabelDocument(self):
        if self.Label is not None:
            return self.Label
        return None

    def SetLabelDocument(self, document):
        self.Label = document

    def GetLabelDocumentJson(self):
        if self.Label is not None:
            return self.Label.ToJson()
        return None

    def GetLabelMediaType(self):
        if self.Label is not None:
            return self.Label.GetMediaType()
        return None

    def GetValidation(self):
        if self.Validation is not None:
            return self.Validation
        return None

    def GetValidationJson(self):
        if self.Validation is not None:
            return self.Validation.ToJson()
        return None

    def SetValidation(self, validation):
        self.Validation = validation

    def ToJson(self):
        return {
            'label': {
                'type': str(self.GetLabelMediaType()),
                'value':
                self.GetLabelDocumentJson()
            },
            'validation': self.GetValidationJson()
        }


class InputDocument(_InputDocument):

    Type = MediaType.Parse(_InputDocument.MIME_TYPE)
