from mediaType import MediaType
from document import Document
from datetime import datetime
from functools import reduce


class _PaymentInvoiceDocument(Document):

    MIME_TYPE = 'application/vnd.lime.invoice+json'

    def __init__(self, currency, dueTo, items=[]):
        super().__init__(MediaType.Parse(_PaymentInvoiceDocument.MIME_TYPE))

        self.SetItems(items)
        self.SetDueTo(dueTo)
        self.Currency = currency
        self._Created = datetime.now()

    def GetItems(self):
        return self._Items

    def SetItems(self, items):
        for i in items:
            if not isinstance(i, _PaymentInvoiceDocument.Item):
                raise ValueError(
                    'The parameter "items" must be a list of Item Model')
        self._Items = items

    def SetDueTo(self, dueTo):
        if not isinstance(dueTo, datetime):
            raise ValueError('The parameter "dueTo" must be a datetime')
        self._DueTo = dueTo

    @property
    def Total(self):
        total = reduce((lambda x, y: x.Total + y.Total), self._Items)
        if (isinstance(total, _PaymentInvoiceDocument.Item)):
            total = total.Total
        return total

    def GetItemsJson(self):
        return [x.ToJson() for x in self._Items]

    def ToJson(self):
        return {
            'created': self._Created.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'dueTo': self._DueTo.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'currency': self.Currency,
            'total': self.Total,
            'items': self.GetItemsJson()
        }

    class Item:

        def __init__(self, quantity, unit, currency, description):
            self.Quantity = float(quantity)
            self.Unit = float(unit)
            self.Currency = currency
            self.Description = description

        @property
        def Total(self):
            return self.Quantity * self.Unit

        def ToJson(self):
            return {
                'quantity': self.Quantity,
                'unit': self.Unit,
                'currency': self.Currency,
                'total': self.Total,
                'description': self.Description
            }


class PaymentInvoiceDocument(_PaymentInvoiceDocument):

    Type = MediaType.Parse(_PaymentInvoiceDocument.MIME_TYPE)
