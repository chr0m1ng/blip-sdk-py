from requests import session
from lime_python import Node
from extensions.uriTemplates import UriTemplate


class BlipSdk:

    def __init__(self, authorization):
        if authorization[0:3].lower() != 'key':
            authorization = 'Key %s' % authorization
        self.Authorization = authorization
        self.Session = session()
        self.Session.headers.update({'Authorization': authorization})

    if __name__ == "__main__":
        print(UriTemplate.ANALYSIS_FEEDBACK.value.format('test'))
