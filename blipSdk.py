from models.message import Message
from models.node import Node
from requests import session


class BlipSdk:

    def __init__(self, authorization):
        if authorization[0:3].lower() != 'key':
            authorization = 'Key %s' % authorization
        self.Authorization = authorization
        self.Session = session()
        self.Session.headers.update({'Authorization': authorization})
