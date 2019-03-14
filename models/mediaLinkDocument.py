from mediaType import MediaType
from document import Document


class _MediaLinkDocument(Document):

    MIME_TYPE = 'application/vnd.lime.media-link+json'

    def __init__(self, mimeType=None, size=None, aspectRatio=None, uri=None,
                 title=None, text=None, previewType=None, previewUri=None):
        super().__init__(MediaType.Parse(_MediaLinkDocument.MIME_TYPE))

        self.MimeType = mimeType
        self.Size = size
        self.AspectRatio = aspectRatio
        self.Uri = uri
        self.Title = title
        self.Text = text
        self.PreviewType = previewType
        self.PreviewUri = previewUri

    def ToJson(self):
        json = {
            'uri': self.Uri
        }
        if self.MimeType is not None:
            json.update({'type': self.MimeType})
        if self.Text is not None:
            json.update({'text': self.Text})
        if self.Size is not None:
            json.update({'size': self.Size})
        if self.AspectRatio is not None:
            json.update({'aspectRatio': self.AspectRatio})
        if self.Title is not None:
            json.update({'title': self.Title})
        if self.PreviewType is not None:
            json.update({'previewType': self.PreviewType})
        if self.PreviewUri is not None:
            json.update({'previewUri': self.PreviewUri})

        return json


class MediaLinkDocument(_MediaLinkDocument):

    Type = MediaType.Parse(_MediaLinkDocument.MIME_TYPE)
