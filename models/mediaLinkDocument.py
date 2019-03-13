from mediaType import MediaType
from document import Document


class MediaLinkDocument(Document):

    MIME_TYPE = 'application/vnd.lime.media-link+json'

    def __init__(self, mimeType=None, size=None, aspectRatio=None, uri=None,
                 tittle=None, text=None, previewType=None, previewUri=None):
        super().__init__(MediaType.Parse(MediaLinkDocument.MIME_TYPE))

        self.MimeType = mimeType
        self.Size = size
        self.AspectRatio = aspectRatio
        self.Uri = uri
        self.Tittle = tittle
        self.Text = text
        self.PreviewType = previewType
        self.PreviewUri = previewUri

    @property
    def Type():
        return MediaType.Parse(MediaLinkDocument.MIME_TYPE)

    def ToJson(self):
        json = {
            'uri': self.Uri
        }
        if self.MimeType is not None:
            json.update({'type': self.MimeType})
        if self.Size is not None:
            json.update({'size': self.Size})
        if self.AspectRatio is not None:
            json.update({'aspectRatio': self.AspectRatio})
        if self.Tittle is not None:
            json.update({'tittle': self.Tittle})
        if self.PreviewType is not None:
            json.update({'previewType': self.PreviewType})
        if self.PreviewUri is not None:
            json.update({'previewUri': self.PreviewUri})

        return json
