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


class InputDocument(Document):

    MIME_TYPE = 'application/vnd.lime.input+json'

    def __init__(self, label=None, validation=None):
        super().__init__(MediaType.Parse(InputDocument.MIME_TYPE))

        if isinstance(label, str):
            label = PlainTextDocument(label)
        self.Label = label  # PlainText
        if isinstance(validation, Validation):
            self.Validation = validation
        elif validation is not None:
            raise ValueError(
                'The parameter "validation" must be a Validation Model')

    def GetLabelDocument(self):
        return self.Label

    def SetLabelDocument(self, document):
        self.Label = document

    def GetLabelDocumentJson(self):
        return self.Label.ToJson()

    def GetLabelMediaType(self):
        return self.Label.GetMediaType()

    def GetValidation(self):
        return self.Validation

    def GetValidationJson(self):
        return self.Validation.ToJson()

    def SetValidation(self, validation):
        self.Validation = validation

    @staticmethod
    def Type():
        return MediaType.Parse(InputDocument.MIME_TYPE)

    def ToJson(self):
        return {
            'label': {
                'type': str(self.GetLabelMediaType()),
                'value':
                self.GetLabelDocumentJson()
            },
            'validation': self.GetValidationJson()
        }
