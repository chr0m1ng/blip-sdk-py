from document import Document
from mediaType import MediaType
from enum import Enum


class ChatState(Enum):

    Starting = 'starting'
    Composing = 'composing'
    Paused = 'paused'
    Deleting = 'deleting'
    Gone = 'gone'


class ChatStateDocument(Document):

    MIME_TYPE = 'application/vnd.lime.chatstate+json'

    def __init__(self, chatState=None):
        super().__init__(MediaType.Parse(ChatStateDocument.MIME_TYPE))
        self.State = chatState

    @property
    def Type():
        return MediaType.Parse(ChatStateDocument.MIME_TYPE)

    def ToJson(self):
        return {
            'state': self.State
        }
