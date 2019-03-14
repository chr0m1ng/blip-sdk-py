from document import Document
from mediaType import MediaType
from enum import Enum


class ChatState(Enum):

    Starting = 'starting'
    Composing = 'composing'
    Paused = 'paused'
    Deleting = 'deleting'
    Gone = 'gone'


class _ChatStateDocument(Document):

    MIME_TYPE = 'application/vnd.lime.chatstate+json'

    def __init__(self, chatState=None):
        super().__init__(MediaType.Parse(_ChatStateDocument.MIME_TYPE))
        self.State = chatState

    def ToJson(self):
        return {
            'state': self.State
        }


class ChatStateDocument(_ChatStateDocument):

    Type = MediaType.Parse(_ChatStateDocument.MIME_TYPE)
