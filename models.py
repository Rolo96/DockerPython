from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField,
    ListField, ReferenceField, StringField,IntField
)

class Product(Document):
    meta = {'collection': 'product'}
    name = StringField()
    code = IntField()
    amount = IntField()
    cost = IntField()
