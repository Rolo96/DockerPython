from mongoengine import connect

from models import Product

connect(host='mongomock://localhost')


def init_db():
    test = Product(name='Test', code = 1, amount = 1, cost = 1)
    test.save()
