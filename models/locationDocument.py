from mediaType import MediaType
from document import Document


class _LocationDocument(Document):

    MIME_TYPE = 'application/vnd.lime.location+json'

    def __init__(self, text=None, latitude=None,
                 longitude=None, altitude=None):
        super().__init__(MediaType.Parse(_LocationDocument.MIME_TYPE))
        self.Text = text
        self.Latitude = latitude
        self.Longitude = longitude
        self.Altitude = altitude

    def ToJson(self):
        return {
            'latitude': self.Latitude,
            'longitude': self.Longitude,
            'altitude': self.Altitude,
            'text': self.Text
        }


class LocationDocument(_LocationDocument):

    Type = MediaType.Parse(_LocationDocument.MIME_TYPE)
