class Reason:

    def __init__(self, code=None, description=None):
        self.Code = code  # reasonCode
        self.Description = description  # String

    def __str__(self):
        return '%s (Code %d)' % (self.Description, self.Code)

    def __repr__(self):
        return str(self)

    def ToJson(self):
        return {
            'code': self.Code,
            'description': self.Description
        }
