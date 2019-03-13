from document import Document
from mediaType import MediaType


class PlainTextDocument(Document):

    def __init__(self, value=None):
        super().__init__(MediaType.TextPlain)
        self.Value = value

    @staticmethod
    def Type():
        return MediaType.TextPlain

    def __str__(self):
        return str(self.Value)

    def ToJson(self):
        return str(self.Value)  # For plain/text we only need the text itself
